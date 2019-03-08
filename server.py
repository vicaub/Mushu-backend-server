from flask import Flask, request, render_template, jsonify
from cfp import make_response
from equivalent import get_equiv_carbone
from errors.cfp_errors import APICallError, ProductNotFoundError, APIResponseError
from errors.flask_errors import ApplicationError
import traceback

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
    except Exception as ex:
        print(''.join(traceback.format_exception(etype=type(ex), value=ex, tb=ex.__traceback__)))
        raise ApplicationError("Une erreur est survenue lors du calcul de l'empreinte carbone, veuillez vous adressez à l'équipe Mushu",
                               payload={"barcode": barcode})


@app.route("/equivalent")
def get_equivalent():
    try:
        cfp = float(request.args.get('cfp'))
        unit = request.args.get('unit')
        if unit == 'g':
            cfp /= 1000
        equivalent = get_equiv_carbone(cfp)
        return jsonify(equivalent)
    except (APICallError, ProductNotFoundError, APIResponseError) as e:
        try:
            message = e.message
        except:
            message = str(e)
        raise ApplicationError(message, payload={"cfp": cfp, "unit": unit})
    except Exception as ex:
        print(''.join(traceback.format_exception(etype=type(ex), value=ex, tb=ex.__traceback__)))
        raise ApplicationError("Une erreur est survenue lors du calcul de votre équivalent carbone, veuillez vous adressez à l'équipe Mushu",
                               payload={"cfp": cfp, "unit": unit})


if __name__ == "__main__":
    app.run(debug=True)
