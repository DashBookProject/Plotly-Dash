import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from pandas_datareader import wb


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

indicators = ['pop % using internet', 'parliament seats % held by women',
              'CO2 emissions (kt)']

# get country name and ISO id for mapping on choropleth
countries = wb.get_countries()
countries['capitalCity'].replace({'':None}, inplace=True)
countries.dropna(subset=['capitalCity'], inplace=True)
countries = countries[['name', 'iso3c']]
countries = countries[countries['name'] != 'Kosovo']
countries = countries.rename(columns={'name': 'country'})


def update_wb_data():
    # Retrieve specific world bank data from API
    df = wb.download(indicator=['IT.NET.USER.ZS','SG.GEN.PARL.ZS',
                                'EN.ATM.CO2E.KT'],
                     country=countries['iso3c'], start=2005, end=2016)
    df = df.reset_index()
    df.year = df.year.astype(int)

    # Add country ISO3 id to main df
    df = pd.merge(df, countries, on='country')
    df = df.rename(
            columns={'IT.NET.USER.ZS':'pop % using internet',
                     'SG.GEN.PARL.ZS':'parliament seats % held by women',
                     'EN.ATM.CO2E.KT':'CO2 emissions (kt)'}
    )
    return df


app.layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col([
                html.H1('Analysis of World Bank Data',
                        style={'textAlign':'center'}),
                dcc.Graph(
                    id='my-choropleth',
                    figure={}
                ),
            ], width=12)
        ),
        dbc.Row(
            dbc.Col([
                dbc.Label('World Bank Indicator to map:',
                          className="font-weight-bold",
                          style={'textDecoration':'underline',
                                 'fontSize':20}
                          ),
                dcc.RadioItems(
                    id='radio-indicator',
                    options=[{'label': i, 'value': i} for i in indicators],
                    value='pop % using internet',
                ),
            ], width=4)
        ),
        dbc.Row([
            dbc.Col([
                dbc.Label('Year to map:',
                          className="font-weight-bold",
                          style={'textDecoration':'underline',
                                 'fontSize':20}
                          ),
                dcc.RangeSlider(
                    id='years-range',
                    min=2005,
                    max=2016,
                    step=1,
                    value=[2005,2006],
                    marks={
                        2005:"2005", 2006:"06'", 2007:"07'",
                        2008:"08'", 2009:"09'", 2010:"10'",
                        2011:"11'", 2012:"12'", 2013:"13'",
                        2014:"14'", 2015:"15'", 2016:"2016"
                    }
                ),
                html.Br(),
                dbc.Button(id='my-button', children='Submit', n_clicks=0,
                           color="primary", className="mr-1"),
            ], width=6),
        ]),

        dcc.Store(id='storage', storage_type='local', data={}),
        dcc.Interval(id='timer', interval=1000*60, n_intervals=0)
    ]
)


@app.callback(
    Output(component_id='storage', component_property='data'),
    Input(component_id='timer', component_property='n_intervals')
)
def store_data(n_time):
    dataframe = update_wb_data()
    return dataframe.to_dict('records')


@app.callback(
    Output(component_id='my-choropleth', component_property='figure'),
    Input(component_id='my-button', component_property='n_clicks'),
    State(component_id='years-range', component_property='value'),
    State(component_id='radio-indicator', component_property='value'),
    State(component_id='storage', component_property='data')
)
def update_graph(n_clicks, years_chosen, indct_chosen, stored_dataframe):
    dff = pd.DataFrame.from_records(stored_dataframe)

    if years_chosen[0] != years_chosen[1]:
        years_range = range(years_chosen[0], years_chosen[1]+1)
        years_range = list(years_range)
        dff = dff[dff['year'].isin(years_range)]
        dff = dff.groupby(['iso3c','country'])[indct_chosen].mean()
        dff = dff.reset_index()

        fig = px.choropleth(dff, locations='iso3c', color=indct_chosen,
                            scope="world",
                            hover_data={'iso3c':False, 'country':True},
                            labels={"parliament seats % held by women":
                                    "% parliament women"}
                            )
        fig.update_layout(geo={'projection': {'type': 'natural earth'}},
                          margin=dict(l=50, r=50, t=50, b=50))
        return fig

    if years_chosen[0] == years_chosen[1]:
        dff = dff[dff['year'].isin(years_chosen)]
        fig = px.choropleth(dff, locations='iso3c', color=indct_chosen,
                            scope="world",
                            hover_data={'iso3c':False, 'country':True},
                            labels={"parliament seats % held by women":
                                    "% parliament women"}
                            )
        fig.update_layout(geo={'projection': {'type': 'natural earth'}},
                          margin=dict(l=50, r=50, t=50, b=50))
        return fig


if __name__ == "__main__":
    app.run_server(debug=True)
