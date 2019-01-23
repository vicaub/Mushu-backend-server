from flask import Flask, request, render_template

from carbon_footprint_calculator import get_cfp_from_barcode

app = Flask(__name__)


@app.route("/cfp")
def get_cfp():
    # TODO: check request query params
    barcode = request.args.get('barcode')
    result = get_cfp_from_barcode(barcode)
    return result


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run()
