from flask import redirect, render_template, url_for, request, session
from flask import current_app as app
import requests

#!\GitHub\SDV-API\plotlyflask\plotlydash
# from plotlydash import dashboard
from plotlydash import test

API = "http://sdv-api.herokuapp.com/"
# print(test.a)


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
    # global number_of_records
    number_of_records = request.form.get('number_records')

    if int(request.form.get('format_selection')) == 1:  # JSON
        return redirect(url_for('json_data', length=number_of_records))
    else:
        SDV(number_of_records)
        return redirect(url_for('/dashapp/<length>/', length=number_of_records))


@app.route('/json/<length>', methods=['GET', 'POST'])
def json_data(length=0):
    response = requests.get(API + str(length)).json()
    return response
