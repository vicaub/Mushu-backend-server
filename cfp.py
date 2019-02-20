import traceback

import requests

from errors.cfp_errors import ProductNotFoundError, APICallError, APIResponseError
from models.Ingredient import Ingredient
from models.Matching import Matching

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
        cfp = round(matching.compute_footprint(),2)

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
        response["quantity_value"] = off_response["product"]["product_quantity"]
        response["quantity_string"] = off_response["product"]["quantity"]
        response["image_url"] = off_response["product"]["image_url"]
    except KeyError:
        raise APIResponseError()

    response = {**get_cfp(off_response), **response}

    return response
