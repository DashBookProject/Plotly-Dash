from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.DataFrame(
    {
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
    }
)

fig = px.bar(df, x="Fruit", y="Amount", color="City")

app.layout = html.Div(
    [
        html.H1("Fruit Analysis App", style={"textAlign": "center"}),
        dcc.Graph(id="example-graph", figure=fig),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
