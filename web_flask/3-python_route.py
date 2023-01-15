#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """function that displays: Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """function that displays: HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """function that displays: C <text>"""
    return 'C %s' % text.replace("_", " ")


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python',
           defaults={"text": "is cool"}, strict_slashes=False)
def python(text):
    """function that displays: Python <text>"""
    return 'Python %s' % text.replace("_", " ")


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
