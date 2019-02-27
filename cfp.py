import traceback

import requests

from errors.cfp_errors import ProductNotFoundError, APICallError, APIResponseError
from models.Ingredient import Ingredient
from models.Matching import Matching
import re

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
        return {"value": float(cf_value), "unit": cf_unit, "cfp_in_api": True}
    except KeyError:
        # We need to compute manually CFP
        ingredient_string = off_response["product"]["ingredients_text"]
        ingredient = Ingredient(off_response["product"]["product_name"], ingredient_string, percent=100)
        ingredient.update_percent()

        matching = Matching(ingredient)
        cfp = matching.compute_footprint()

        return {"value": cfp, "unit": "kg/kg", "cfp_in_api": False, "ingredients": str(ingredient)}


def make_response(barcode):
    response = {"barcode": barcode}

    try:
        off_response = openfoodfacts_api(barcode)
    except Exception:
        raise APICallError()

    if off_response["status"] == 0:
        raise ProductNotFoundError()

    try:
        response["name"] = off_response["product"]["product_name"]
        response["original_ingredients"] = off_response["product"]["ingredients_text"]
        response["quantity_string"] = off_response["product"]["quantity"]
        response["image_url"] = off_response["product"]["image_url"]
        dico = build_weight(off_response["product"]["quantity"])
        response.update(dico)

    except KeyError:
        raise APIResponseError()

    response = {**get_cfp(off_response), **response}

    return response

def build_weight(quantity_string, dictionnaire = {}):
    list_unities_re = re.compile(r"g|kg|mg|l|cl|dl|ml")
    if re.search('\d+',quantity_string.lower()):
        qte = re.search('\d+',quantity_string.lower())
        dictionnaire["weight"] = float(qte[0])
        qte_unit_string = quantity_string[qte.span()[1]:].lower()

        if list_unities_re.search(qte_unit_string):
            qte_unit = list_unities_re.search(qte_unit_string)
            dictionnaire["weightUnit"] = qte_unit[0]
        else:
            raise ValueError("L'unitée n'est pas connue")
    else:
        raise ValueError("Il n'y a pas de chiffre indiquant la quantité")
    return dictionnaire


if __name__ == "__main__":
    res = make_response(str(3229820795676))
    print(res)
    res_2 = make_response(str(3033490306014 ))
    print(res_2)
    res_3 = make_response(str(3324498000746))
    print(res_3)

