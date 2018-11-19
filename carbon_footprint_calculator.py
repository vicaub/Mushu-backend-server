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

        print(response["product"]["categories"].split(","))
        print(response["product"]["ingredients"])




if __name__ == "__main__":
    # get_product_from_barcode("3700214611548")
    get_product_from_barcode("3103220009574")



