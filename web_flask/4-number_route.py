#!/usr/bin/python3
""" a script that starts a Flask web application """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    ''' displays "Hello HBNB!" for route: / '''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello():
    ''' displays "HBNB" for route: /hbnb '''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cfun(text):
    ''' displays "C" followed by value of the text variable '''
    txt = text.replace('_', " ")
    return "C {}". format(txt)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    ''' displays "Python" followed by the value of the text '''
    txt = text.replace('_', " ")
    return "Python {}". format(txt)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    ''' dipslays "n is a number" only if n is an integer '''
    return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)