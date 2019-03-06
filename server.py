from flask import Flask, request, render_template, jsonify
from cfp import make_response
from equivalent import get_equiv_carbone
from errors.cfp_errors import APICallError, ProductNotFoundError, APIResponseError
from errors.flask_errors import ApplicationError

app = Flask(__name__)


# Server error handling

@app.errorhandler(ApplicationError)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.errorhandler(404)
def page_not_found(e):
    """
    Called when user call an undeclared route
    """
    return render_template('404.html'), 404


# Routes

@app.route("/cfp")
def process_barcode():
    try:
        barcode = request.args.get('barcode')
        result = make_response(barcode)
        return jsonify(result)
    except (APICallError, ProductNotFoundError, APIResponseError) as e:
        try:
            message = e.message
        except:
            message = str(e)
        raise ApplicationError(message, payload={"barcode": barcode})


@app.route("/equivalent")
def get_equivalent():
    cfp = float(request.args.get('cfp'))
    equivalent = get_equiv_carbone(cfp)
    return jsonify(equivalent)


if __name__ == "__main__":
    app.run(debug=True)
