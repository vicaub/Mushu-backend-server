from flask import Flask, request

from carbon_footprint_calculator import get_cfp_from_barcode

app = Flask(__name__)


@app.route("/cfp")
def get_cfp():
    # TODO: check request query params
    barcode = request.args.get('barcode')
    result = get_cfp_from_barcode(barcode)
    return result


if __name__ == "__main__":
    app.run()
