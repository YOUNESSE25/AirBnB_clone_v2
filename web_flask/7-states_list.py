#!/usr/bin/python3
'''script that starts a Flask web application:'''
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
'''Flask app'''
app.url_map.strict_slashes = False


@app.teardown_appcontext
def flask_close_db(exc):
    '''close session sqlalchemist'''
    storage.close()

@app.route('/states_list')
def states_list():
    """display a HTML page"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
