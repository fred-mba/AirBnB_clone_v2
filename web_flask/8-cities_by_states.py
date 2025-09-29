#!/usr/bin/python3
"""List cities by states"""

from flask import Flask, render_template
from models import storage, City, State


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    """List cities by state name in relation to storage engine type"""
    if hasattr(storage, "_DBStorage__session"):
        state_dict = storage.all(State)
        city_dict = storage.all(City)
    return render_template(
        '8-cities_by_states.html',
        states=state_dict,
        cities=city_dict
    )


@app.teardown_appcontext
def teardown_appctx(exception):
    """Remove DB session after each request"""
    storage.close()


if __name__ == "__main___":
    app.run(host='0.0.0.0', port='5000')
