from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import plotly.express as px
import pandas as pd

# add the dbc.css Stylesheet to your app and choose a theme
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css"
app = Dash(__name__, external_stylesheets=[dbc.themes.VAPOR, dbc_css])
load_figure_template(["vapor"])

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group", template="vapor")

app.layout = dbc.Container([
    html.H1("Hello Dash", style={'textAlign': 'center'}),
    html.P("Type anything here:"),
    dcc.Input(className="mb-2"),
    dcc.Graph(
        id='example-graph',
        figure=fig

    )
],
    fluid=True,
    className="dbc"
)

if __name__ == '__main__':
    app.run_server(debug=True)
