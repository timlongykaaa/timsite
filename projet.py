import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime, time


data = pd.read_csv('/home/ec2-user/projetlinux/data1.csv', delimiter=';', header=None, names = ['price','date'])
data['price'] = data['price'].str.replace('€', '')
data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d %H:%M:%S')



# Initialize the app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div(children=[
    html.H1(children='Graphique du prix de l\'Ethereum'),
    dcc.Graph(id='ethereum-graph'),
    dcc.Interval(id='graph-update', interval=1000*60*5, n_intervals=0)])


# Define the callback function to update the graph
@app.callback(Output('ethereum-graph', 'figure'),
              [Input('graph-update', 'n_intervals')])


def update_graph(n):
    # Sélectionner les données les plus récentes
    recent_data = data[data['date'] > (datetime.now() - pd.Timedelta(minutes=5))]
    x = recent_data['date']
    y = recent_data['price']

    # Créer la figure pour le graphique
    fig = {
        'data': [{
            'x': x,
            'y': y,
            'type': 'line',
            'name': 'Prix de l\'Ethereum'
        }],
        'layout': {
            'title': 'Prix de l\'Ethereum en fonction du temps',
            'xaxis': {'title': 'Date'},
            'yaxis': {'title': 'Prix'}
        },
    } 
    return fig   


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, host = "0.0.0.0", port = 9400)






