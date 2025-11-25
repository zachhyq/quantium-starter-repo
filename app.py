

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('data/processed_data.csv')

fig = px.line(df, x='date', y='sales', labels={'date': "Date", 'sales': "Sales($)"})

app.layout = html.Div(children=[
    html.H1(children='Visualising Sales across Time'
            ,style={'textAlign': 'center'}),



    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)