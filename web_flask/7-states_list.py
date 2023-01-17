#!/usr/bin/python3
''' a script that starts a Flask web application '''

from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    ''' listing state in db storage '''
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def shut_db(exc):
    ''' removing SQLAlchemy Session after each request '''
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
