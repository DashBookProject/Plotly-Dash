# import ipdb
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = px.data.tips()
print(df.head())

app = Dash(__name__)

app.layout = html.Div([
    html.Div(id='graph-placeholder'),
    dcc.Dropdown(id='size-selected',
                 value='Female',
                 options=[{'label': x, 'value': x} for x in df.sex.unique()])
])

@app.callback(
    Output('graph-placeholder', 'children'),
    Input('size-selected', 'value')
)
def update_graph(value):
    # ipdb.set_trace()
    dff = df[df.sex==value]
    dff = dff[dff.day=='Mon']
    fig = px.bar(dff, x='time', y='total_bill')
    my_graph = dcc.Graph(figure=fig)

    return my_graph


if __name__ == '__main__':
    app.run_server(debug=False, threaded=False, port=8000)
