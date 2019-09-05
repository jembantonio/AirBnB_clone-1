#!/usr/bin/python3
''' starts a flask web application
'''
from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes=False


@app.route('/states')
@app.route('/states_list')
def display_states():
    return render_template(
            '7-states_list.html', state_list=storage.all('State'))


@app.route('/cities_by_states')
def display_city_by_states():
    return render_template(
            '8-cities_by_states.html',
            state_list=storage.all('State'),
            city_list=storage.all('City'))


@app.route('/states/<state_id>')
def select_state_display_cities(state_id):
    states = storage.all('State').values()
    for state in states:
        if state.id == state_id:
            return render_template('9-states.html', state=state)
    return render_template('9-state.html', state=None)


@app.teardown_appcontext
def teardown(self):
    storage.close()


if __name__ == '__main__':
    storage.close()
    app.run(host='0.0.0.0', port='5000')
