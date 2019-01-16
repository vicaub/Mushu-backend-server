import requests
from pprint import pprint

from Ingredient import Ingredient
from Matching import Matching

off_url = "https://fr.openfoodfacts.org/api/v0/produit/"


def get_product_from_api(barcode):
    request_url = off_url + barcode + ".json"

    response = requests.get(request_url).json()

    return response


def get_cfp_from_barcode(barcode):
    off_response = get_product_from_api(barcode)
    product_name = off_response["product"]["product_name"]
    print(product_name)
    try:
        # CFP already in API response
        cf_value = off_response["product"]["nutriments"]["carbon-footprint"]
        cf_unit = off_response["product"]["nutriments"]["carbon-footprint_unit"]
        return cf_value, cf_unit
    except:
        # We need to compute manually CFP
        ingredient_string = off_response["product"]["ingredients_text"]

        ingredient = Ingredient(product_name, ingredient_string, percent=100)
        ingredient.update_percent()

        matching = Matching()

        cfp = matching.compute_footprint(ingredient)

        return cfp, "kg/kg"



if __name__ == "__main__":
    test_barcodes = ["3700214611548", "3103220009574", "3250391587285", "3017800022016", "9002490100070", "3588570001995"]

    for barcode in test_barcodes:
        print(get_cfp_from_barcode(barcode))


