from dash import dash, Dash, html, dcc
from flask import request, session
import plotly.express as px
import requests

# from plotlyflask.routes import number_of_records


def SDV(number_of_records):
    API = "http://sdv-api.herokuapp.com/"

    ######## Find the inputs in html and request it from API or generate v2 ########
    # number_of_records = request.args.get('records') or 0
    print(number_of_records)

    ######## V2 SDV - read JSON -> df -> plotly timeline ########
    records = requests.get(API).json()
    df = []
    for i in records['sleep_record'][-number_of_records:]:
        record = dict(Date='{}/{}'.format(i['date']['month'], i['date']['day']),
                      Sleep='2022-02-01 {}:{}:00'.format(
            i['sleep']['hour'], i['sleep']['min']),
            Wake='2022-02-01 {}:{}:00'.format(
            i['wake']['hour'], i['wake']['min']),
            Duration=i['duration'])
        df.append(record)
    global fig
    fig = px.timeline(df, color="Duration", x_start="Sleep",
                      x_end="Wake", y="Date", color_continuous_scale=['#ffff3f', '#52b69a', '#0077b6'],
                      height=20*len(records['sleep_record']), width=800)
    fig.update_yaxes(autorange="reversed")


def init_dashboard(server):
    # number_of_records = request.args['messages']
    # number_of_records = session['messages']
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/<length>/'
    )

    dash_app.layout = html.Div(children=[
        dcc.Graph(
            id='sdv-plot',
            figure=fig
        )
    ])

    return dash_app.server
