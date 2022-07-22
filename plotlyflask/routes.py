from flask import Flask, redirect, render_template, url_for, request, session
from flask import current_app as app
from numpy import number
import requests

from . import dashboard
from .dashboard import init_dashboard


API = "http://sdv-api.herokuapp.com/"


@app.route('/')
def home():
    return render_template(
        'index.html',
        title="Plotly Dash in Flask",
        description="Embed Plotly Dash into Flask application",
        template="home-template",
        body="This is a homepage served with Flask"
    )


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    global number_of_records
    try:
        number_of_records = int(request.form.get('number_records'))
    except:
        number_of_records = -1
    if (number_of_records > 0):
        print("submit: " + str(number_of_records))
        if request.form.get('format_selection') == '1':  # JSON
            print("JSON")
            return redirect(url_for('json_data', length=number_of_records))
        elif request.form.get('format_selection') == '2': # Image
            print("IMAGE")
            dashboard.SDV(number_of_records)
            return redirect(url_for('/dashapp/'))
        else: # Rerun home
            return redirect(url_for('home'))
    else:  # Rerun home
        return redirect(url_for('home'))

@app.route('/json/<length>', methods=['GET', 'POST'])
def json_data(length=0):
    response = requests.get(API + str(length)).json()
    return response
