import requests
from pprint import pprint

off_url = "https://ssl-api.openfoodfacts.org/api/v0/produit/"


def get_product_from_barcode(barcode):
    request_url = off_url + barcode + ".json"

    response = requests.get(request_url).json()

    try:

        cf_value = response["product"]["nutriments"]["carbon-footprint"]
        cf_unit = response["product"]["nutriments"]["carbon-footprint_unit"]

    except:

        print(response["product"]["ingredients_text_with_allergens"])
        return(response["product"]["ingredients_text_with_allergens"])
        #print(response["product"]["categories"].split(","))
        #print(response["product"]["ingredients"])

def get_aliment_from_str(str_aliment):
    res = str_aliment.find('courgette')
    print(res)




if __name__ == "__main__":
    get_product_from_barcode("3700214611548")
    get_product_from_barcode("3103220009574")
    get_aliment_from_str(get_product_from_barcode("3083680659062")) # Modifier la fiche Courgettes cuisinées à la Provençale




