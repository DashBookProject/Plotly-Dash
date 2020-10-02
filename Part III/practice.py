import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly_express as px
import dash_bootstrap_components as dbc
import pandas as pd

external_stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = px.data.gapminder()

my_text = dcc.Markdown(
    """
    ## Dash Boostrap Practice App
    
    This app is a quickstart to developing your own app    
    - Use this Markdown component for your own text.  You can  
    learn more about how to format text such as  adding **bold** and 
    *italics*  [here](https://commonmark.org/help/tutorial/)    
    -  Use the cards  to create components and then add them to the layout.
    This figure is from the [Plotly Tutorial](https://plotly.com/python/plotly-express/)
    
"""
)

fig = px.area(df, x="year", y="pop", color="continent", line_group="country")

text_card = html.Div(
    dbc.Card(
        dbc.CardBody(
            [html.H4(" Card Title", className="card-title"), my_text,],
            className="mt-4",
        )
    )
)

graph_card = html.Div(
    dbc.Card(
        dbc.CardBody(
            [
                html.H4(" Card Title", className="card-title"),
                dcc.Graph(id="my_graph", figure=fig,),
            ],
            className="mt-4",
        )
    )
)

app.layout = dbc.Container(
    dbc.Row([dbc.Col(text_card, width=6), dbc.Col(graph_card, width=6),])
)

if __name__ == "__main__":
    app.run_server(debug=True)
