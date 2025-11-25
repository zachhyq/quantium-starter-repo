

from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)


df = pd.read_csv('data/processed_data.csv')

init_fig = px.line(df, x='date', y='sales', labels={'date': "Date", 'sales': "Sales($)"})

app.layout = html.Div(
    className="container mx-auto p-4 font-sans",
    children=[
        html.H1(children='Visualising Sales across Time',
                className="text-3xl font-extrabold text-center mb-6 text-indigo-700 tracking-tight"),

        html.Br(),
        html.Div(
            className="flex justify-center mb-6",
            children=[
                html.Label(
                    'Select Region',
                    className="mr-4 font-semibold text-gray-700"
                    ),
                dcc.RadioItems(id = 'region-radio',
                       options=['North', 'South', 'East', 'West', 'All'],
                       value='all',
                       className="flex space-x-4",
                       labelClassName="cursor-pointer hover:text-indigo-600 transition duration-150 ease-in-out"
                       ),

            ]
        ),
        html.Br(),

        dcc.Graph(
            id='sales-graph',
            figure=init_fig,
            className="bg-gray-100 rounded-lg shadow-xl p-2"
        )
    ]
)

#Update function
@callback(
    Output('sales-graph', 'figure'),
    Input('region-radio', 'value')
)
def update_graph(region):
    region = region.lower()
    if region != 'all':
        df_select = df[df['region'] == region]
    else:
        df_select = df
    fig = px.line(df_select, x='date', y='sales', labels={'date': "Date", 'sales': "Sales($)"})
    return fig

if __name__ == '__main__':
    app.run(debug=True)