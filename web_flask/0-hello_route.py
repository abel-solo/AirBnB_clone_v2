#!/usr/bin/python3
""" starts a flask web application """


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """ prints Hello HBNB """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
