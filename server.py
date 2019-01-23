from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/cfp")
def get_cfp():
    return "Hello World"


if __name__ == "__main__":
    app.run()
