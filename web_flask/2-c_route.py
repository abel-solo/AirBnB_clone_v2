#!/usr/bin/python3
"""  script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    ''' display "Hello HBNB!" for / '''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    ''' display "HBNB" for /hbnb '''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cfun(text):
    '''display "C" followed by the value of the text variable'''
    txt = text.replace('_', " ")
    return "C {}". format(txt)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
