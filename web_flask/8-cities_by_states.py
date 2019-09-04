#!/usr/bin/python3
''' starts a flask web application
'''
from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def display_states():
    return render_template(
            '7-states_list.html', state_list=storage.all('State'))


@app.route('/cities_by_states', strict_slashes=False)
def display_city_by_states():
    return render_template(
            '8-cities_by_states.html',
            state_list=storage.all('State'),
            city_list=storage.all('City'))


@app.teardown_appcontext
def teardown(self):
    storage.close()


if __name__ == '__main__':
    storage.close()
    app.run(host='0.0.0.0', port='5000')
