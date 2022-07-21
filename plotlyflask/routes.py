from flask import render_template
from flask import current_app as app
import requests

API = "http://sdv-api.herokuapp.com/"


@app.route('/')
def home():
    return render_template(
        'index.html',
        title="Plotly Dash in Flask",
        description="Embed Plotly Dash into Flask application",
        template="home-template",
        body="This is a homepage servef with Flask"
    )


@app.route('/json')
def json_data():
    response = requests.get(API).json()
    return response
