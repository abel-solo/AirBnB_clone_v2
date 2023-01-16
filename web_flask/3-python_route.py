#!/usr/bin/python3
""" script that starts a Flask web application """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    ''' displays "Hello HBNB!" for / '''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello():
    ''' displays "HBNB" for /hbnb '''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cfun(text):
    ''' displays "c" followed by value of the text vriable '''
    txt = text.replace('_', " ")
    return "C {}". format(txt)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    ''' displays "python" followed by the value of the text '''
    txt = text.replace('_', " ")
    return "Python {}". format(txt)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
