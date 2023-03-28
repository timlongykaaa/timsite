import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime, time


app = dash.Dash(__name__)

df = pd.read_csv('/home/ec2-user/projetlinux/data1.csv', delimiter=';', names=['Prix', 'Date'])
df['Prix'] = df['Prix'].str.replace('€', '')
df['Date'] = pd.to_datetime(df['Date'])


app.layout = html.Div(children=[
    html.H1(children="Welcome to Tim's webpage, find below the Ethereum live price",style={'textAlign': 'center'} ),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                go.Scatter(
                    x=df['Date'],
                    y=df['Prix'],
                    mode='lines'
                )
            ],
            'layout': go.Layout(
                xaxis={'title': 'Date'},
                yaxis={'title': 'Prix'}
            )
        }
    ),
    dcc.Interval(
        id='interval-component',
        interval=5*60*1000, # in milliseconds
        n_intervals=0
    )
])


@app.callback(Output('example-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])


def update_graph(n):
    #lecture du fichier csv
    df = pd.read_csv('/home/ec2-user/projetlinux/data1.csv', delimiter=';', names=['Prix', 'Date'])
    df['Prix'] = df['Prix'].str.replace('€', '')
    df['Date'] = pd.to_datetime(df['Date'])
    #creation du graphique
    fig = {'data': [go.Scatter(x=df['Date'], y=df['Prix'], mode='lines')],
           'layout': go.Layout(xaxis ={'title':'Date'},yaxis = {'title' : 'Prix'})}
    return fig

#go.Layout(xaxis=dict(range=[min(df['Date']), max(df['Date'])]), yaxis=dict(range=[min(df['Prix']), max(df['Prix'])]))

if __name__ == '__main__':
    app.run_server(debug=True, host = "0.0.0.0", port = 9400)




