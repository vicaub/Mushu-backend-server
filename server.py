from flask import Flask, request, render_template, jsonify
from cfp import make_response
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


if __name__ == "__main__":
    app.run(debug=True)
