
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
df = pd.DataFrame({
    "A": [1, 3, 4, 6, 8, 2],
    "B": [4, 1, 2, 2, 4, 5],
    "C": [5, 3, 6, 0, 2, 4]
})

labels = {"A": "Group 1", "B": "Group 2", "C": "Group 3"}

#fig = px.line(df, y=["A", "B", "C"], labels=labels)




fig = px.pie(names=["Cash", "Bonds", "Stocks"], values =[0,10,90],
             color_discrete_map={'Cash': "#3cb521",
                                 'Bonds': "#f5b668",
                                 'Stocks': "#3399f3"},
             title='my pie',
             height=375,
             )
fig.update_traces(textposition='inside', textinfo='percent+label')

fig.update_layout(
         title_x=0.5,
         margin=dict(b=25, t=75, l=35, r=25),
         paper_bgcolor="whitesmoke",
     )




#px.pie( color_discrete_map=)
# def make_pie(slider_input, title):
#     colors = ["#3cb521", "#f5b668", "#3399f3"]
#     fig = go.Figure(
#         data=[
#             go.Pie(
#                 labels=["Cash", "Bonds", "Stocks"],
#                 values=slider_input,
#                 textinfo="label+percent",
#                 textposition="inside",
#                 marker=dict(colors=colors),
#                 sort=False,
#             )
#         ]
#     )
#     fig.update_layout(
#         title_text=title,
#         title_x=0.5,
#         margin=go.layout.Margin(b=25, t=75, l=35, r=25),
#         height=375,
#         paper_bgcolor="whitesmoke",
#     )
#     return fig




app.layout = html.Div(

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
)

if __name__ == '__main__':
    app.run_server(debug=True)
