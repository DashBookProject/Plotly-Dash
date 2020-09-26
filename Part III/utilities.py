import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


navbar = dbc.NavbarSimple(
    [
        dbc.NavItem(dbc.NavLink('Historic Returns', href="/page/historic")),
        dbc.NavItem(dbc.NavLink('Stock Quotes', href="/page/quotes")),
        dbc.NavItem(dbc.NavLink('About', href="/page/about")),
    ],
    brand="Wealth Management Dashboard",
    brand_style={'font-size': 'x-large'},
    brand_href="#",
    color="primary",
    fluid=True,
    dark=True,
)

footer = html.Div(
    dcc.Markdown(
        '''
         This information is intended solely as general information for educational
        and entertainment purposes only and is not a substitute for professional advice and
        services from qualified financial services providers familiar with your financial
        situation.

         Questions?  Suggestions? Please don't hesitate to get in touch: [Email](mailto:awardapps@fastmail.com?subject=cool)
        '''
    ),
    className='m5 pl-5 pr-5 bg-primary text-white'
)

######## Markdown content


asset_allocation_text = dcc.Markdown(
    """
    **Asset allocation** is one of the main factors that determines your portfolio returns
    and volatility over time.  Play with the app and see for yourself!

    See "My Portfolio",   the dashed line in the graph, and watch how
    your results change as you move the sliders to select different asset
    allocations. You can enter different starting times and dollar amounts too.
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
