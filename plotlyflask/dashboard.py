from dash import dash, Dash, html, dcc
import plotly.express as px
import requests
import pandas as pd


df1 = pd.DataFrame([
    dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28'),
    dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
    dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30')
])

fig = px.timeline(df1, x_start="Start", x_end="Finish", y="Task")

API = "http://sdv-api.herokuapp.com/"
df = []


def SDV(number_of_records):

    ######## Find the inputs in html and request it from API or generate v2 ########
    print("SDV:", number_of_records)

    ######## V2 SDV - read JSON -> df -> plotly timeline ########
    records = requests.get(API).json()
    for i in records['sleep_record'][-number_of_records:]:
        record = dict(Date='{}/{}'.format(i['date']['month'], i['date']['day']),
                      Sleep='2022-02-01 {}:{}:00'.format(
            i['sleep']['hour'], i['sleep']['min']),
            Wake='2022-02-01 {}:{}:00'.format(
            i['wake']['hour'], i['wake']['min']),
            Duration=i['duration'])
        df.append(record)

    fig = px.timeline(df, color="Duration", x_start="Sleep", x_end="Wake", y="Date", color_continuous_scale=[
                      '#ffff3f', '#52b69a', '#0077b6'], height=20*len(df), width=800)
    fig.update_yaxes(autorange="reversed")


def init_dashboard(server):
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/'
    )

    dash_app.layout = html.Div(children=[
        dcc.Graph(
            id='sdv-plot',
            figure=fig
        ),
        html.Button('Generate', id='generate-image')
    ])

    return dash_app.server
