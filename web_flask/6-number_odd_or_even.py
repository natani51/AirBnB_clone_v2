#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, escape, render_template
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
    return 'C %s'.replace("_", " ") % escape(text)


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python',
           defaults={"text": "is cool"}, strict_slashes=False)
def python(text):
    """function that displays: Python <text>"""
    return 'Python %s'.replace("_", " ") % escape(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """function that displays: number <text>"""
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """function that display a template"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_template_even_odd(n):
    """function that display a template"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
