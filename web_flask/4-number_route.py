#!/usr/bin/python3
"""script that starts a flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def web_hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def web_hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def web_c(text):
    space = text.replace('_', ' ')
    return f"C {space}"


@app.route("/python", strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def web_python(text="is cool"):
    space_2 = text.replace('_', ' ')
    return f"Python {space_2}"


@app.route("/number/<int:n>", strict_slashes=False)
def web_number(n):
    if type(n) == int:
        return f"{n} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
