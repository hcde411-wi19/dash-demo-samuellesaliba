# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)


app.layout = html.Div([
    dcc.Graph(
        id='',
        figure={
            'data': [{'marker': {'color': 'red', 'size': '5', 'symbol': 104},
   'text': ['My family and cousin', 'My family, cousin, and friend', 'My family (but not me) and my friend', 'My family without me', 'My family without me or my brother'],
   'type': 'scatter',
   'x': [2014, 2015, 2016, 2017, 2018],
   'y': [6, 7, 5, 4, 3]}],
 'layout': {'title': 'People Living in My Childhood Home Each Year in December',
  'xaxis': {'title': '# of People'},
  'yaxis': {'title': 'Year'}}
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

