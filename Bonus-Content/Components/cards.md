# Plotly Dash Bootstrap Card Components

### Welcome to the bonus content of "The Book of Dash".  :hugs:

Here you will find additional examples of Plotly Dash components, layouts and style.  To learn more about making
dashboards with Plotly Dash, and how to buy your copy of ["The Book of Dash"](https://nostarch.com/book-dash), please see the reference section
at the bottom of this article.

This article will focus on the Card components from the Dash Boostrap Component library. Using cards is a great way to 
create eye-catching content. We'll show you how to make the card content interactive with callbacks, but first we'll
focus on the style and layout.


## Plotly Dash app with a Bootstrap Card 

We'll start with the basics - a minimal Dash app to display a single card without any additional styling. Be sure to check out 
the complete reference for [using Dash Bootstrap cards.](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/card/)


Next we'll show how to jazz it up to make it look better  -- and more importantly  -- so it conveys key information at a glance. 

![simple card](https://user-images.githubusercontent.com/72614349/193452367-c222b23b-5e11-4398-a150-2c3f9df72ad3.png)

```python
from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB, dbc.icons.BOOTSTRAP])

card =  dbc.Card(
    dbc.CardBody(
        [
            html.H1("Sales"),
            html.H3("$104.2M")
        ],
    ),
)

app.layout=dbc.Container(card)

if __name__ == "__main__":
    app.run_server(debug=True)
```

## Styling a Dash Bootstrap Card

An easy way to style content is by using Boostrap utility classes.  See the all the utility
classes at the [Dash Bootstrap Cheatsheet](https://dashcheatsheet.pythonanywhere.com/) app. This handy cheatsheet is
made by a co-author of “The Book of Dash”.


In this card we center the text and change the color with "text-center" and "text-success". The Bootstrap themes have 
named colors and "success" is a shade of green. For more information about styling your app with a Boostrap theme, see [Dash Bootstrap Theme Explorer](https://hellodash.pythonanywhere.com/)



![card-style](https://user-images.githubusercontent.com/72614349/193453405-5b80ba60-484f-4cab-97bb-7e4d84f4a7a9.png)


```python
card =  dbc.Card(
    dbc.CardBody(
        [
            html.H1("Sales"),
            html.H3("$104.2M", className="text-success")
        ],
    ),
    className="text-center"
)
```

Feel free to watch Adam’s explainer [video](https://www.youtube.com/watch?v=vqVwpL4bGKY&t=16s) on Bootstrap and styling 
your app if you need to get up to speed! 

## Dash Bootstrap Card with Icons

You can add Bootstrap and/or Font Awesome icons to your Dash Bootstrap components. In this example, we will add the bank icon as well as change the background color using the Bootstrap utility class `bg-primary`.


![card-with-icons](https://user-images.githubusercontent.com/72614349/195423112-8f1ed8ab-9c99-4219-99c2-9f70df3a4f14.png)

```python
card = dbc.Card(
    dbc.CardBody(
        [
            html.H1([html.I(className="bi bi-bank me-2"), "Profit"]),
            html.H3("$8.3M"),
            html.H4(html.I("10.3% vs LY", className="bi bi-caret-up-fill text-success")),
        ],
    ),
    className="text-center m-4 bg-primary text-white",
)

```

To learn more, see the 
[Icons](https://dash-bootstrap-components.opensource.faculty.ai/docs/icons/) section of the dash-bootstrap-components
documentation.  You can also find more information about adding icons to dash components in the [buttons article](https://github.com/DashBookProject/Plotly-Dash/blob/master/Bonus-Content/Components/buttons.md#dash-bootstrap-dbcbutton-with-icons).


## Dash Bootstrap Cards Side-by-Side 

In business intelligence dashboards, it's common to highlight KPIs or Key Performance Indicators in a group of cards.  You can find many
examples in the [Plotly App Gallery](https://dash.gallery/Portal/).  

This app places three KPI cards side-by-side.  We use the `dbc.Row` and `dbc.Col` components to create this responsive
card layout.  When you run this app, try changing the width of the browser window to see how the cards expand 
to fill the row based on the screen size. 

This app also demonstrates the usage of Bootstrap `border` utility classes to add and style a border.  Here we add a border on the left
 and change the color to highlight the results.  Another trick is to use the "text-nowrap" class to keep the icon
and the text together on the same line when the cards shrink to accommodate small screen sizes.

![row with cards](https://user-images.githubusercontent.com/72614349/194442282-bbf646bb-b724-4ba8-af17-dac18be29315.png)
```python

from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB, dbc.icons.BOOTSTRAP])


card_sales = dbc.Card(
    dbc.CardBody(
        [
            html.H1([html.I(className="bi bi-currency-dollar me-2"), "Sales"], className="text-nowrap"),
            html.H3("$106.7M"),
            html.Div(
                [
                    html.I("5.8%", className="bi bi-caret-up-fill text-success"),
                    " vs LY",
                ]
            ),
        ], className="border-start border-success border-5"
    ),
    className="text-center m-4"
)


card_profit = dbc.Card(
    dbc.CardBody(
        [
            html.H1([html.I(className="bi bi-bank me-2"), "Profit"], className="text-nowrap"),
            html.H3("$8.3M",),
            html.Div(
                [
                    html.I("12.3%", className="bi bi-caret-down-fill text-danger"),
                    " vs LY",
                ]
            ),
        ], className="border-start border-danger border-5"
    ),
    className="text-center m-4",
)


card_orders = dbc.Card(
    dbc.CardBody(
        [
            html.H1([html.I(className="bi bi-cart me-2"), "Orders"], className="text-nowrap"),
            html.H3("91.4K"),
            html.Div(
                [
                    html.I("10.3%", className="bi bi-caret-up-fill text-success"),
                    " vs LY",
                ]
            ),
        ], className="border-start border-success border-5"
    ),
    className="text-center m-4",
)

app.layout = dbc.Container(
    dbc.Row(
        [dbc.Col(card_sales), dbc.Col(card_profit), dbc.Col(card_orders)],
    ),
    fluid=True,
)


if __name__ == "__main__":
    app.run_server(debug=True)

```

## Creating Dash Bootstrap Cards in a Loop

In the previous example, notice that a lot of the code for creating the card is the same.  To reduce the amount of 
repetitive code, let's create cards in a function.  

In this app, we introduce the `dbc.CardHeader` component and the `"shadow"` class to style the card.  We'll show you how
to add more style later in the app that displays crypto prices.

![cards in a loop](https://user-images.githubusercontent.com/72614349/193834232-9b558741-8288-4667-8ff7-9de346e62945.png)

```python
from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

summary = {"Sales": "$100K", "Profit": "$5K", "Orders": "6K", "Customers": "300"}


def make_card(title, amount):
    return dbc.Card(
        [
            dbc.CardHeader(html.H2(title)),
            dbc.CardBody(html.H3(amount, id=title)),
        ],
        className="text-center shadow",
    )


app.layout = dbc.Container(
    dbc.Row([dbc.Col(make_card(k, v)) for k, v in summary.items()], className="my-4"),
    fluid=True,
)


if __name__ == "__main__":
    app.run_server(debug=True)

```

## Dash Bootstrap Card with an Image

This card uses the `dbc.CardImage` component.  This is a great format for the "who's who" section of your app.  It
works well for displaying information about products too. 

![card with image](https://user-images.githubusercontent.com/72614349/194618466-b1e0a06e-38d6-44cf-824e-0a6d01417f18.png)

```python

from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

count = "https://user-images.githubusercontent.com/72614349/194616425-107a62f9-06b3-4b84-ac89-2c42e04c00ac.png"

card = dbc.Card([
    dbc.CardImg(src=count, top=True),
    dbc.CardBody(
        [
            html.H3("Count von Count", className="text-primary"),
            html.Div("Chief Financial Officer"),
            html.Div("Sesame Street, Inc.", className="small"),
        ]
    )],
    className="shadow my-2",
    style={"maxWidth": 350},
)


app.layout=dbc.Container(card)

if __name__ == "__main__":
    app.run_server(debug=True)

```



## Dash Bootstrap Card with an Image and a Link

This app has a card with the `dbc.CardLink` component.  When you run this app, try clicking on either the logo or the title.
You will see that both are links to the Plotly site displaying the current job openings.  We do this by including both the
`html.Img` component with the Plotly logo and the `html.Span` with the title in the `dbc.CardLink` component.


![card with link and image](https://user-images.githubusercontent.com/72614349/194613328-940714ce-2841-4d48-a6e8-c81e59b5e5d1.png)
```python

from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

plotly_logo_dark = "https://user-images.githubusercontent.com/72614349/182967824-c73218d8-acbf-4aab-b1ad-7eb35669b781.png"

card = dbc.Card(
    dbc.CardBody(
        [
            dbc.CardLink(
                [
                    html.Img(src=plotly_logo_dark, height=65),
                    html.Span("Plotly Job Openings", className="ms-2")
                ],
                className="text-decoration-none h2",
                href="https://plotly.com/careers/"
            ),
            html.Hr(),
            html.Div("Engineering", className="h3"),
            html.Div("Intermediate Backend Engineer", className="text-danger"),
            html.Div("Remote, Canada", className="small"),
        ]
    ),
    className="shadow my-2",
    style={"maxWidth": 450},
)


app.layout=dbc.Container(card)

if __name__ == "__main__":
    app.run_server(debug=True)

```

## Dash Bootstrap Card with a Background Image

This app puts the image in the background and uses the `dbc.CardImgOverlay` component to place content on top of the
image.  We also use `dbc.Button`s to link to other sites for more information.  See the buttons article for more information.
Be sure to run the app and check out the links.  The Webb Telescope app is pretty cool!



![card with background image](https://user-images.githubusercontent.com/72614349/194621648-6454f8da-8787-4918-9d41-82984ef37b49.png)

```python

from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB, dbc.icons.BOOTSTRAP])

webb_deep_field = "https://user-images.githubusercontent.com/72614349/192781103-2ca62422-2204-41ab-9480-a730fc4e28d7.png"
card = dbc.Card(
    [
        dbc.CardImg(src=webb_deep_field),
        dbc.CardImgOverlay([
            html.H2("James Webb Space Telescope"),
            html.H3("First Images"),
            html.P(
                "Learn how to make an app to compare before and after images of Hubble vs Webb with ~40 lines of Python",
                style={"marginTop":200}

            ),
            dbc.Button("See the App", href="https://jwt.pythonanywhere.com/"),
            dbc.Button(
                [html.I(className="bi bi-github me-2"), "source code"],
                className="ms-2 text-white",
                href="https://github.com/AnnMarieW/webb-compare",

            )
        ])

    ],
    style={"maxWidth": 500},
    className="my-4 text-center text-white"
)

app.layout=dbc.Container(card)

if __name__ == "__main__":
    app.run_server(debug=True)

```

See this Plotly Dash app live:  https://jwt.pythonanywhere.com/  


![jwt](https://user-images.githubusercontent.com/72614349/194623180-4aab626b-095e-490c-89eb-84730364db0a.gif)


## Plotly Dash App with Live Updates

This app shows live updates of crypto prices.  We use a `dcc.Interval` component to fetch the data from CoinGecko every 
6 seconds.  The CoinGecko API is easy to use because you don't need an API key,  and it's
free if you keep the number of updates within the free tier limits.   We pull the current price, 24 hour price change 
and the coin logo from the data feed and display the data in a nicely styled card.   

In this app we introduce callbacks to update the data, and show how to get the data from CoinGecko.  All the other styling
has been covered in previous examples.   Note that in this app, the color of the text and the up and down arrows are updated
dynamically based on the data in the `make_card` function.

![live_crypto_prices](https://user-images.githubusercontent.com/72614349/195419638-7214c1d2-deb7-4697-b1b4-4c064cf6af8a.png)

```python
import dash
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import requests

app = Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO, dbc.icons.BOOTSTRAP])

coins = ["bitcoin", "ethereum", "binancecoin", "ripple"]
interval = 6000 # update frequency - adjust to keep within free tier
api_url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"


def get_data():
    try:
        response = requests.get(api_url, timeout=1)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(e)


def make_card(coin):
    change = coin["price_change_percentage_24h"]
    price = coin["current_price"]
    color = "danger" if change < 0 else "success"
    icon = "bi bi-arrow-down" if change < 0 else "bi bi-arrow-up"
    return dbc.Card(
        html.Div(
            [
                html.H4(
                    [
                        html.Img(src=coin["image"], height=35, className="me-1"),
                        coin["name"],
                    ]
                ),
                html.H4(f"${price:,}"),
                html.H5(
                    [f"{round(change, 2)}%", html.I(className=icon), " 24hr"],
                    className=f"text-{color}",
                ),
            ],
            className=f"border-{color} border-start border-5",
        ),
        className="text-center text-nowrap my-2 p-2",
    )


mention = html.A(
    "Data from CoinGecko", href="https://www.coingecko.com/en/api", className="small"
)
interval = dcc.Interval(interval=interval)
cards = html.Div()
app.layout = dbc.Container([interval, cards, mention], className="my-5")


@app.callback(Output(cards, "children"), Input(interval, "n_intervals"))
def update_cards(_):
    coin_data = get_data()
    if coin_data is None or type(coin_data) is dict:
        return dash.no_update
    
    # make a list of cards with updated prices
    coin_cards = []
    updated = None
    for coin in coin_data:
        if coin["id"] in coins:
            updated = coin.get("last_updated")
            coin_cards.append(make_card(coin))

    # make the card layout
    card_layout = [
        dbc.Row([dbc.Col(card, md=3) for card in coin_cards]),
        dbc.Row(dbc.Col(f"Last Updated {updated}")),
    ]
    return card_layout


if __name__ == "__main__":
    app.run_server(debug=True)


```


## Plotly Dash App with a Sidebar

A common layout for Dash apps is to put inputs in a sidebar, and the output in the main section of the page.  We can place
both the sidebar and the output in Dash Boostrap Card components.  

See the app and the code live at the [Dash Example Index](https://dash-example-index.herokuapp.com/histograms)

![histogram](https://user-images.githubusercontent.com/72614349/194643421-bdc784b6-769c-4230-a25b-e1048b9e7aaf.gif)



## Plotly Dash Example Index

See more examples of interactive apps in the [Dash Example Index](https://dash-example-index.herokuapp.com)

![Example Index](https://user-images.githubusercontent.com/72614349/192155573-39042b8f-0c54-479d-bd96-fa0eb3b96f06.png)




## Reference


### [Dash documentation - tutorial](https://dash.plotly.com/).  Getting Started with Dash

### [Dash Example Index](https://dash-example-index.herokuapp.com/?code=button).  Sample apps with buttons

### [Dash Bootstrap Components documentation](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/card/) - dbc.Card

### [Dash Bootstrap Theme Explorer](https://hellodash.pythonanywhere.com/). A guide for styling Plotly Dash apps with a Bootstrap theme

## [Order Your Copy of "The Book of Dash" Today!](https://nostarch.com/book-dash)
![The Book Of Dash](https://user-images.githubusercontent.com/72614349/185497519-733bdfc3-5731-4419-9a68-44c1cad04a78.png)

### Authors

__Ann Marie Ward__:

👩‍💻 GitHub: https://github.com/AnnMarieW
💬 Dash Forum: https://community.plotly.com/u/annmariew/summary

__Adam Schroeder__:

▶️ YouTube CharmingData: https://www.youtube.com/c/CharmingData

__Chris Mayer__:

🐍 Python + Crypto Email Academy: https://blog.finxter.com/subscribe/_


