# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash_table
import dash_table.FormatTemplate as FormatTemplate

import pandas as pd
import pathlib
import plotly.graph_objects as go


FONT_AWESOME = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"

external_stylesheets = [dbc.themes.SPACELAB, FONT_AWESOME]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# set relative path
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("./data").resolve()

#  make dataframe from  spreadsheet:
df = pd.read_excel(DATA_PATH.joinpath("historic.xlsx"))


MAX_YR = df.Year.max()
MIN_YR = df.Year.min()

# since data is as of year end, need to add start year
df = (
    df.append({"Year": MIN_YR - 1}, ignore_index=True)
    .sort_values("Year", ignore_index=True)
    .fillna(0)
)


"""
==========================================================================
Tables
"""


total_returns_table = html.Div(
    [
        dash_table.DataTable(
            id="total_returns",
            columns=[{"id": "Year", "name": "Year", "type": "text"}]
            + [
                {
                    "id": col,
                    "name": col,
                    "type": "numeric",
                    "format": FormatTemplate.money(0),
                }
                for col in ["Cash", "Bonds", "Stocks", "Total"]
            ],
            style_table={
                "overflowY": "scroll",
                "border": "thin lightgrey solid",
                "maxHeight": "425px",
            },
            style_cell={"textAlign": "right", "font-family": "arial"},
            style_cell_conditional=[{"if": {"column_id": "Year"}, "type": "text"}],
        )
    ]
)

annual_returns_pct_table = html.Div(
    [
        dash_table.DataTable(
            id="annual_returns_pct",
            columns=(
                [{"id": "Year", "name": "Year", "type": "text"}]
                + [
                    {
                        "id": col,
                        "name": col,
                        "type": "numeric",
                        "format": FormatTemplate.percentage(1),
                    }
                    for col in df.columns[1:]
                ]
            ),
            style_cell={"textAlign": "right", "font-family": "arial"},
            style_table={
                "overflowY": "scroll",
                "border": "thin lightgrey solid",
                "maxHeight": "400px",
            },
            data=df.to_dict("records"),
        )
    ],
)


def make_summary_table(dff):
    """  Make table to show cagr and  best and worst periods"""

    start_yr = dff["Year"].iat[0]
    end_yr = dff["Year"].iat[-1]

    table_header = [
        html.Thead(
            html.Tr(
                [
                    html.Th(" "),
                    html.Th(" "),
                    html.Th(f"Annual returns (CAGR) from {start_yr} to {end_yr}"),
                    html.Th(f"Worst Year from {start_yr} to {end_yr}"),
                ]
            )
        )
    ]
    row1 = html.Tr(
        [
            html.Td("Cash"),
            html.Td(
                html.I(className="fa fa-money-bill-alt", style={"font-size": "150%"})
            ),
            html.Td(cagr(dff["All_Cash"])),
            html.Td(worst(dff, "3-mon T.Bill")),
        ],
    )

    # to save space, row2, row3, row4 are not displayed, but they are
    # defined similar to row1 above

    row2 = html.Tr(
        [
            html.Td("Bonds"),
            html.Td(html.I(className="fa fa-handshake", style={"font-size": "150%"})),
            html.Td(cagr(dff["All_Bonds"])),
            html.Td(worst(dff, "10yr T.Bond")),
        ],
    )
    row3 = html.Tr(
        [
            html.Td("Stocks"),
            html.Td(html.I(className="fa fa-industry ", style={"font-size": "150%"})),
            html.Td(cagr(dff["All_Stocks"])),
            html.Td(worst(dff, "S&P 500")),
        ],
    )
    row4 = html.Tr(
        [
            html.Td("Inflation"),
            html.Td(html.I(className="fa fa-ambulance", style={"font-size": "150%"})),
            html.Td(cagr(dff["Inflation_only"])),
            html.Td(" "),
        ],
    )
    table_body = [html.Tbody([row1, row2, row3, row4], className="text-center")]
    summary_table = dbc.Table(
        table_header + table_body,
        bordered=True,
        responsive=True,
        style={"backgroundColor": "whitesmoke"},
    )
    return summary_table


"""
==========================================================================
Figures
"""

#######  Pie chart
def make_pie(slider_input, title):
    colors = ["#3cb521", "#f5b668", "#3399f3"]
    fig = go.Figure(
        data=[
            go.Pie(
                labels=["Cash", "Bonds", "Stocks"],
                values=slider_input,
                textinfo="label+percent",
                textposition="inside",
                marker=dict(colors=colors),
                sort=False,
            )
        ]
    )
    fig.update_layout(
        title_text=title,
        title_x=0.5,
        margin=go.layout.Margin(b=25, t=75, l=35, r=25),
        height=375,
        paper_bgcolor="whitesmoke",
    )
    return fig


# =======  Line chart
def make_returns_chart(dff):
    start = dff.loc[1, "Year"]
    x = dff["Year"]
    yrs = dff["Year"].size - 1
    title = f"Returns for {yrs} years starting {start}"
    dtick = 1 if yrs < 16 else 2 if yrs in range(16, 30) else 5

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=x, y=dff["All_Cash"], name="All Cash", marker=dict(color="#3cb521")
        )
    )
    fig.add_trace(
        go.Scatter(
            x=x,
            y=dff["All_Bonds"],
            name="All Bonds (10yr T.Bonds)",
            marker=dict(color="#d47500"),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=x,
            y=dff["All_Stocks"],
            name="All Stocks (S&P500)",
            marker=dict(color="#3399f3"),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=x,
            y=dff["Total"],
            name="My Portfolio",
            marker=dict(color="black"),
            line=dict(width=6, dash="dot"),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=x,
            y=dff["Inflation_only"],
            name="Inflation",
            visible=True,
            marker=dict(color="#cd0200"),
        )
    )
    fig.update_layout(
        title=title,
        template="none",
        showlegend=True,
        legend=dict(x=0.01, y=0.99),
        height=400,
        margin=dict(l=40, r=10, t=60, b=30),
        yaxis=dict(tickprefix="$", fixedrange=True),
        xaxis=dict(title="Year Ended", fixedrange=True, dtick=dtick),
    )
    return fig


"""
==========================================================================
Markdown Text
"""

datasource_text = dcc.Markdown(
    """    
    [Data source:](http://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html)
    Historical Returns on Stocks, Bonds and Bills from NYU Stern School of
    Business
    """
)

asset_allocation_text = dcc.Markdown(
    """

> **Asset allocation** is One of the main factors that determines your 
  portfolio returns and volatility over time.  Play with the app and see
  for yourself!

> See "My Portfolio",   the dashed line in the graph, and watch how
  your results change as you move the sliders to select different asset
  allocations. You can enter different starting times and dollar amounts 
  too.
"""
)


backtesting_text = dcc.Markdown(
    """

    Past performance certainly does not determine future results.... but you can still
    learn a lot by reviewing how various asset classes have performed over time.

    Use the sliders to change the asset allocation (how much you invest in cash vs
    bonds vs stock) and see how this affects your returns.

    Note that the results shown in "My Portfolio" assumes rebalancing was done at
    the beginning of every year.  Also, this information is based on the S&P 500 index
    as a proxy for "stocks", the 10 year US Treasury Bond for "bonds" and the 3 month
    US Treasury Bill for "cash."  Your results of course,  would be different based
    on your actual holdings.

    This is intended to help you determine your investment philosophy and understand
    what sort of risks and returns you might see for each asset category.

    The  data is from [Aswath Damodaran](http://people.stern.nyu.edu/adamodar/New_Home_Page/home.htm)
    who teaches  corporate finance and valuation at the Stern School of Business
    at New York University.

    Check out his excellent on-line course in
    [Investment Philosophies.](http://people.stern.nyu.edu/adamodar/New_Home_Page/webcastinvphil.htm)
    """
)


footer = html.Div(
    dcc.Markdown(
        """
         This information is intended solely as general information for educational
        and entertainment purposes only and is not a substitute for professional advice and
        services from qualified financial services providers familiar with your financial
        situation.    Questions?  Suggestions? Please don't hesitate to get in touch:
          [Email](mailto:awardapps@fastmail.com?subject=cool)
        """
    ),
    className="p-2 pl-5 pr-5 bg-primary text-white",
)


"""
==========================================================================
Make Tabs
"""


# =======Play tab components

asset_allocation_card = html.Div(
    dbc.Card(
        dbc.CardBody(html.Div(html.Div(asset_allocation_text, className="ml-3 mt-2"),)),
        className="mt-4",
    )
)

slider_card = html.Div(
    dbc.Card(
        dbc.CardBody(
            [
                html.H4("First set cash allocation %:", className="card-title"),
                dcc.Slider(
                    id="cash",
                    marks={i: f"{i}%" for i in range(0, 101, 10)},
                    min=0,
                    max=100,
                    step=5,
                    value=10,
                    included=False,
                    persistence=True,
                    persistence_type="session",
                ),
                html.H4("Then set stock allocation % ", className="card-title mt-3",),
                html.Div("(The rest will be bonds)", className="card-title"),
                dcc.Slider(
                    id="stock_bond",
                    marks={i: f"{i}%" for i in range(0, 91, 10)},
                    persistence=True,
                    persistence_type="session",
                    min=0,
                    max=90,
                    step=5,
                    value=50,
                    included=False,
                ),
            ],
        ),
        className="mt-4",
    )
)

inflation_checkbox = html.Div(
    dcc.Checklist(
        id="inflation",
        persistence=True,
        persistence_type="session",
        labelClassName="m-2",
        inputClassName="mr-3",
        options=[{"label": "Include inflation on graph", "value": "Yes",}],
        value=["Yes"],
    )
)


time_period_card = html.Div(
    dbc.Card(
        [
            html.H4("Or check out one of these time periods:", className="card-title"),
            dcc.RadioItems(
                id="select_timeframe",
                options=[
                    {"label": "2007-2008 Great Financial Crisis", "value": "2007"},
                    {"label": "2000 Dotcom Bubble peak", "value": "1999"},
                    {"label": "1970s Energy Crisis", "value": "1970"},
                    {"label": "1929 start of Great Depression", "value": "1929"},
                    {"label": "1928-2019", "value": "1928"},
                ],
                labelStyle={"display": "block"},
                labelClassName="m-2",
                inputClassName="mr-3",
                value="2007",
            ),
        ],
        body=True,
        className="mt-4",
    )
)

amount_input_card = html.Div(
    dbc.Card(
        [
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon("Start Amount $ :", addon_type="prepend"),
                    dbc.Input(
                        id="starting_amount",
                        placeholder="$",
                        type="number",
                        persistence=True,
                        persistence_type="session",
                        min=0,
                        value=10000,
                    ),
                ],
                className="mb-3",
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon("Number of Years:", addon_type="prepend"),
                    dbc.Input(
                        id="planning_time",
                        placeholder="#yrs",
                        type="number",
                        persistence=True,
                        persistence_type="session",
                        min=1,
                        value=13,
                    ),
                ],
                className="mb-3",
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon("Start Year:", addon_type="prepend"),
                    dbc.Input(
                        id="start_yr",
                        placeholder=f"{MIN_YR} to {MAX_YR}",
                        type="number",
                        persistence=True,
                        persistence_type="session",
                        min=MIN_YR,
                        max=MAX_YR,
                        value=2007,
                    ),
                ],
                className="mb-3",
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon("My Portfolio Results: ", addon_type="prepend"),
                    dbc.Input(id="results", type="text", disabled=True,),
                ],
                className="mb-3",
                style={"width": "375px"},
            ),
        ],
        body=True,
        className="mt-4",
    )
)

# =====  Results Tab components

results_card = html.Div(
    dbc.Card(
        [
            dbc.CardHeader("My Portfolio Returns - Rebalanced Annually"),
            dbc.CardBody(total_returns_table),
        ],
        outline=True,
        className="mt-4",
    )
)

data_source_card = html.Div(
    dbc.Card(
        [
            dbc.CardHeader("Source Data: Annual Total Returns",),
            dbc.CardBody(annual_returns_pct_table),
        ],
        outline=True,
        className="mt-4",
    )
)

# ========= Learn Tab  Components
learn_card = html.Div(
    dbc.Card(
        [
            dbc.CardHeader("An Introduction to Backtesting",),
            dbc.CardBody(backtesting_text),
        ],
        outline=True,
        className="mt-4",
    )
)

##==========Build tabs
tabs = html.Div(
    dbc.Tabs(
        [
            dbc.Tab(
                learn_card,
                tab_id="tab1",
                label="Learn",
                label_style={"font-size": "150%", "width": "125px"},
            ),
            dbc.Tab(
                [
                    asset_allocation_text,
                    slider_card,
                    amount_input_card,
                    inflation_checkbox,
                    time_period_card,


                ],
                tab_id="tab-2",
                label="Play",
                label_style={"font-size": "150%", "width": "125px"},
            ),
            dbc.Tab(
                [results_card, data_source_card],
                tab_id="tab-3",
                label="Results",
                label_style={"font-size": "150%", "width": "125px"},
            ),
        ],
        id="tabs",
        active_tab="tab-2",
    ),
    style={"minHeight": "800px"},
)

"""
===========================================================================
Main Layout
"""

app.layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.H2(
                    "Asset Allocation Visualizer",
                    className="text-center bg-primary text-white p-2",
                ),
            )
        ),
        dbc.Row(
            [
                dbc.Col(tabs, width={"size": 5, "order": 1}, className="mt-4 border",),
                dbc.Col(
                    [
                        dcc.Graph(id="pie_allocation", className="mb-2"),
                        dcc.Graph(id="returns_chart", className="border"),
                        html.H6(datasource_text),
                        html.Div(id="summary_table"),
                    ],
                    width={"size": 7, "order": 2},
                    className="pt-4 ",
                ),
            ],
            className="ml-4",
        ),
        dbc.Row(dbc.Col(footer, className="mt-5")),
    ],
    fluid=True,
)


"""
==========================================================================
Calculations for  backtest results, cagr and worst periods
"""


def backtest(stocks, cash, start_bal, nper, start_yr, pmt):
    """ calculates the investment returns for user selected asset allocation,
        rebalanced annually
    """

    end_yr = start_yr + nper - 1
    cash_allocation = cash / 100
    stocks_allocation = stocks / 100
    bonds_allocation = (100 - stocks - cash) / 100

    # Select time period - since data is for year end, include year prior
    # for start ie year[0]
    dff = df[(df.Year >= start_yr - 1) & (df.Year <= end_yr)].set_index(
        "Year", drop=False
    )
    dff["Year"] = dff["Year"].astype(int)

    # add columns for My Portfolio returns
    dff["Cash"] = cash_allocation * start_bal
    dff["Bonds"] = bonds_allocation * start_bal
    dff["Stocks"] = stocks_allocation * start_bal
    dff["Total"] = start_bal
    dff["Rebalance"] = True

    # calculate My Portfolio returns
    for yr in dff.Year + 1:
        if yr <= end_yr:
            # Rebalance at the beginning of the period by reallocating
            # last period's total ending balance
            if dff.loc[yr, "Rebalance"]:
                dff.loc[yr, "Cash"] = dff.loc[yr - 1, "Total"] * cash_allocation
                dff.loc[yr, "Stocks"] = dff.loc[yr - 1, "Total"] * stocks_allocation
                dff.loc[yr, "Bonds"] = dff.loc[yr - 1, "Total"] * bonds_allocation

            # calculate this period's  returns
            dff.loc[yr, "Cash"] = dff.loc[yr, "Cash"] * (
                1 + dff.loc[yr, "3-mon T.Bill"]
            )
            dff.loc[yr, "Stocks"] = dff.loc[yr, "Stocks"] * (1 + dff.loc[yr, "S&P 500"])
            dff.loc[yr, "Bonds"] = dff.loc[yr, "Bonds"] * (
                1 + dff.loc[yr, "10yr T.Bond"]
            )
            dff.loc[yr, "Total"] = dff.loc[yr, ["Cash", "Bonds", "Stocks"]].sum()

    dff = dff.reset_index(drop=True)
    columns = ["Cash", "Stocks", "Bonds", "Total"]
    dff[columns] = dff[columns].round(0)

    # create columns for when portfolio is all cash, all bonds or  all stocks,
    #   include inflation too
    #
    # create new df that starts in yr 1 rather than yr 0
    dff1 = (dff[(dff.Year >= start_yr) & (dff.Year <= end_yr)]).copy()
    #
    # calculate the returns in new df:
    columns = ["All_Cash", "All_Bonds", "All_Stocks", "Inflation_only"]
    annual_returns = ["3-mon T.Bill", "10yr T.Bond", "S&P 500", "Inflation"]
    for col, return_pct in zip(columns, annual_returns):
        dff1[col] = round(start_bal * (1 + (1 + dff1[return_pct]).cumprod() - 1), 0)
    #
    # select columns in the new df to merge with original
    dff1 = dff1[["Year"] + columns]
    dff = dff.merge(dff1, how="left")
    # fill in the starting balance for year[0]
    dff.loc[0, columns] = start_bal
    return dff


def cagr(dff):
    """calculate Compound Annual Growth Rate for a series: """

    start_bal = dff.iat[0]
    end_bal = dff.iat[-1]
    planning_time = len(dff) - 1
    cagr_result = ((end_bal / start_bal) ** (1 / planning_time)) - 1
    return f"{cagr_result:.1%}"


def worst(dff, asset):
    """calculate worst returns for asset in selected period
            and format for display panel """

    worst_yr_loss = min(dff[asset])
    worst_yr = dff.loc[dff[asset] == worst_yr_loss, "Year"].iloc[0]
    return f"{worst_yr}:  {worst_yr_loss:.1%}"


"""
==========================================================================
Callbacks
"""


@app.callback(
    Output("pie_allocation", "figure"),
    [Input("stock_bond", "value"), Input("cash", "value")],
)
def update_pie(stocks, cash):
    bonds = 100 - stocks - cash
    slider_input = [cash, bonds, stocks]

    if stocks >= 70:
        investment_style = "Aggressive"
    elif stocks <= 30:
        investment_style = "Conservative"
    else:
        investment_style = "Moderate"
    figure = make_pie(slider_input, investment_style + " Asset Allocation")
    return figure


@app.callback(
    [
        Output("stock_bond", "max"),
        Output("stock_bond", "marks"),
        Output("stock_bond", "value"),
    ],
    [Input("cash", "value")],
    [State("stock_bond", "value")],
)
def update_stock_slider(cash, initial_stock_value):
    max_slider = 100 - int(cash)
    if initial_stock_value > max_slider:
        stocks = max_slider
    else:
        stocks = initial_stock_value

    # formats the slider scale
    if max_slider > 50:
        marks_slider = {i: f"{i}%" for i in range(0, max_slider + 1, 10)}
    elif max_slider <= 15:
        marks_slider = {i: f"{i}%" for i in range(0, max_slider + 1, 1)}
    else:
        marks_slider = {i: f"{i}%" for i in range(0, max_slider + 1, 5)}
    return max_slider, marks_slider, stocks


@app.callback(
    [Output("planning_time", "value"), Output("start_yr", "value")],
    [Input("select_timeframe", "value")],
)
def update_timeframe(selected_yr):
    timeframe = {"2007": 13, "1999": 10, "1970": 10, "1929": 20, "1928": 98}
    return timeframe[selected_yr], selected_yr


@app.callback(
    [
        Output("total_returns", "data"),
        Output("returns_chart", "figure"),
        Output("summary_table", "children"),
        Output("results", "value"),
    ],
    [
        Input("stock_bond", "value"),
        Input("cash", "value"),
        Input("starting_amount", "value"),
        Input("planning_time", "value"),
        Input("start_yr", "value"),
        Input("inflation", "value"),
    ],
)
def update_totals(stocks, cash, start_bal, planning_time, start_yr, inflation):
    pmt = 0
    if start_bal is None:
        start_bal = 0
    if planning_time is None:
        planning_time = 1
    if start_yr is None:
        start_yr = MIN_YR

    # calculate valid time frames and ranges for UI
    max_time = MAX_YR + 1 - int(start_yr)
    planning_time = max_time if planning_time > max_time else planning_time
    if int(start_yr) + planning_time > MAX_YR:
        start_yr = min(df.iloc[-planning_time, 0], MAX_YR)  # 0 is Year column
    start_yr = int(start_yr)

    # create df of backtest results
    dff = backtest(stocks, cash, start_bal, planning_time, start_yr, pmt)

    # create data for  datatable
    data = dff.to_dict("records")

    # create the line chart
    figure = make_returns_chart(dff)
    figure.update_traces(visible=False, selector=dict(name="Inflation"))
    if inflation:
        figure.update_traces(visible=True, selector=dict(name="Inflation"))

    summary_table = make_summary_table(dff)

    results = "${:0,.0f}     {}".format(dff["Total"].iloc[-1], cagr(dff["Total"]))

    return data, figure, summary_table, results


if __name__ == "__main__":
    app.run_server(debug=True)
