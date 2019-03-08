import requests
from errors.cfp_errors import ProductNotFoundError, APICallError, APIResponseError
from models.Ingredient import Ingredient
from models.Matching import Matching
import re
import traceback

off_url = "https://fr.openfoodfacts.org/api/v0/produit/"


def openfoodfacts_api(barcode):
    request_url = off_url + barcode + ".json"
    response = requests.get(request_url).json()
    return response


def get_cfp(off_response):
    try:
        # CFP already in API response
        cf_value = off_response["product"]["nutriments"]["carbon-footprint"]
        cf_unit = off_response["product"]["nutriments"]["carbon-footprint_unit"]
        return {"CFPDensity": float(cf_value), "unit": cf_unit, "cfp_in_api": True}
    except KeyError:
        # We need to compute manually CFP
        ingredient_string = off_response["product"]["ingredients_text"]
        ingredient = Ingredient(off_response["product"]["product_name"], ingredient_string, percent=100)
        ingredient.update_percent()

        matching = Matching(ingredient)
        cfp = matching.compute_footprint()

        return {"CFPDensity": cfp, "cfp_in_api": False, "ingredients": ingredient.to_json()}


def make_response(barcode):
    response = {"barcode": barcode}

    try:
        off_response = openfoodfacts_api(barcode)
    except Exception as ex:
        print(''.join(traceback.format_exception(etype=type(ex), value=ex, tb=ex.__traceback__)))
        raise APICallError()

    if off_response["status"] == 0:
        raise ProductNotFoundError()

    try:
        response["name"] = off_response["product"]["product_name"]
        response["original_ingredients"] = off_response["product"]["ingredients_text"]
        response["image_url"] = off_response["product"]["image_url"]
        quantity_string = off_response["product"]["quantity"]
        response.update(build_weight(quantity_string))

    except KeyError as ex:
        print(''.join(traceback.format_exception(etype=type(ex), value=ex, tb=ex.__traceback__)))
        raise APIResponseError()

    response = {**get_cfp(off_response), **response}

    dico_cfp = change_units(response["CFPDensity"], response["weight"], response["weightUnit"])
    response.update(dico_cfp)

    return response


def build_weight(quantity_string):
    dictionnaire = {}
    list_unities_re = re.compile(r"g|kg|mg|l|cl|dl|ml")
    if re.search('\d+', quantity_string.lower()):
        qte = re.search('\d+,\d+|\d+\.\d+|\d+', quantity_string.lower())
        qte_float = float(qte[0].replace(",", "."))
        dictionnaire["weight"] = qte_float
        qte_unit_string = quantity_string[qte.span()[1]:].lower()

        if list_unities_re.search(qte_unit_string):
            qte_unit = list_unities_re.search(qte_unit_string)
            dictionnaire["weightUnit"] = qte_unit[0]
        else:
            raise ValueError("L'unitée n'est pas connue")
    else:
        raise ValueError("Il n'y a pas de chiffre indiquant la quantité")
    return dictionnaire


def change_units(CFPdensity, weight, weightunit):
    """Calcul de l'empreinte carbone correspondant à la bonne quantité de produit dans une unité pertinente"""
    # Pour les unités de masses (kg, g, mg et celles de volumes appropriées)
    dictionnaire = {}
    if weightunit == "kg":
        truecfp = float(weight) * float(CFPdensity)
        if truecfp >= 1:
            dictionnaire["TotalCFP"] = truecfp
            dictionnaire["CFPUnit"] = "kg"
        else:
            dictionnaire["TotalCFP"] = truecfp * 1000
            dictionnaire["CFPUnit"] = "g"
    elif weightunit == "g" or weightunit == "l":
        truecfp = float(weight) * float(CFPdensity) * 0.001
        if truecfp >= 1:
            dictionnaire["TotalCFP"] = truecfp
            dictionnaire["CFPUnit"] = "kg"
        else:
            dictionnaire["TotalCFP"] = truecfp * 1000
            dictionnaire["CFPUnit"] = "g"
    elif weightunit == "mg" or weightunit == "ml":
        truecfp = float(weight) * float(CFPdensity) * 0.000001
        if truecfp >= 1:
            dictionnaire["TotalCFP"] = truecfp
            dictionnaire["CFPUnit"] = "kg"
        else:
            dictionnaire["TotalCFP"] = truecfp * 1000
            dictionnaire["CFPUnit"] = "g"
    # Pour les unités de volumes restantes(cl)
    elif weightunit == "cl":
        truecfp = float(weight) * float(CFPdensity) * 0.01
        if truecfp >= 1:
            dictionnaire["TotalCFP"] = truecfp
            dictionnaire["CFPUnit"] = "kg"
        else:
            dictionnaire["TotalCFP"] = truecfp * 1000
            dictionnaire["CFPUnit"] = "g"
    return (dictionnaire)
