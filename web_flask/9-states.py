#!/usr/bin/python3
"""script that starts a Flask web application"""
from models import storage
from flask import Flask, escape, render_template
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def closedb(stor):
    """Closes db session"""
    storage.close()


@app.route('/states', strict_slashes=False, defaults={'id': None})
@app.route('/states/<id>', strict_slashes=False)
def states_template_id(id):
    """function that route /states/<id>"""
    state = states = None
    if not id:
        states = list(storage.all(State).values())
    else:
        states = storage.all(State)
        key = "State." + id
        if key in states:
            state = states[key]
        else:
            state = None
        states = []
    return render_template('9-states.html', **locals())

if __name__ == '__main__':
    storage.reload()
    app.run("0.0.0.0", 5000)
