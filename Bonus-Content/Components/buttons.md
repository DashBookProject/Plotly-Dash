# Plotly Dash Button Components

### Welcome to the bonus content of "The Book of Dash".  :hugs:

Here you will find additional examples of Plotly Dash components, layouts and style.  To learn more about making
dashboards with Plotly Dash, and how to buy your copy of ["The Book of Dash"](https://nostarch.com/book-dash), please see the reference section
at the bottom of this article.

This article will focus on the `html.Button` component from Plotly, and easy ways to style a button using the `dbc.Button` 
from the dash-bootstrap-components library or the `dmc.Button` from the dash-mantine-components library.  

A Button is an element a user can click on to take action in an app such as submit a form or generate a report. We will 
show you how to make the button interactive with callbacks, but first we will focus on the style.


## Plotly Dash html.Button

Here is a very simple Dash app.  It just displays a button with the default style of an html button.  

![html-button](https://user-images.githubusercontent.com/72614349/191817552-eef31218-b389-49c6-963b-e4d581afaa9a.png)


```python
from dash import Dash, html

app = Dash(__name__)

button = html.Button("Enter")

app.layout = html.Div(button)

if __name__ == "__main__":
    app.run(debug=True)
```

## Dash Bootstrap dbc.Button

Rather than customizing the style with css, this app uses a button from the `dash-bootstrap-components` library.  You will 
see that the buttons are styled with fonts, colors and other design features of the Bootstrap theme.  

Bootstrap uses a subset of all colors to create a smaller color palette for generating color schemes.  They these colors
have the names "primary", "secondary", "success", "warning", "danger" and "info".  Using the color pallet from the theme
makes it easy to create a beautiful app with a consistent design.  

Note that we use the `className` prop. The "me-1" adds margin so there is space between the buttons.  See the all the
Bootstrap utility classes at the [Dash Bootstrap Cheatsheet](https://dashcheatsheet.pythonanywhere.com/) app. This handy
cheatsheet is made by a co-author of "The Book of Dash".  


![button-bootstrap](https://user-images.githubusercontent.com/72614349/191816622-e70ac131-f0cd-44cc-9b3e-1c568a2dc654.png)
```python
from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

buttons = html.Div(
    [
        dbc.Button("Primary", color="primary", className="me-1" ),
        dbc.Button("Secondary", color="secondary", className="me-1"),
        dbc.Button("Success", color="success", className="me-1"),
        dbc.Button("Warning", color="warning", className="me-1"),
        dbc.Button("Danger", color="danger", className="me-1"),
        dbc.Button("Info", color="info"),
    ], className= "m-4"
)

app.layout = dbc.Container(buttons)

if __name__ == "__main__":
    app.run_server(debug=True)

```

## Dash Bootstrap dbc.Buttons with dark and light themes

You can change the theme of your app with one line of code, simply by changing the `external_stylesheets`. Here are the
buttons with 4 of the 26 themes available in the `dash-bootstrap-components` library.  

Learn more about designing your Dash app with a Bootstrap theme at the [Dash Bootstrap Theme Explorer](https://hellodash.pythonanywhere.com/),
a site made by a co-author of "The Book of Dash".

Cyborg theme:  

![button-cyborg](https://user-images.githubusercontent.com/72614349/191816623-d6dabbf4-0639-467a-a934-ca28b8f0b3c5.png)
```
app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
```
-----------------

Solar theme:  

![buttons-solar](https://user-images.githubusercontent.com/72614349/191816618-a7d4da0f-9caf-4b41-bf48-860eb5f6556f.png)
```
app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
```

---------

Minty theme:  

![button-minty](https://user-images.githubusercontent.com/72614349/191816620-1c0708fd-de53-40c8-9bff-5db9d64d7dff.png)
```
app = Dash(__name__, external_stylesheets=[dbc.themes.MINTY])
```

------------

Sketchy theme:  

![button-sketchy](https://user-images.githubusercontent.com/72614349/191816619-db7c9812-18d2-4d6e-9d34-51e0dabdee90.png)
```
app = Dash(__name__, external_stylesheets=[dbc.themes.SKETCHY])
```





## Dash Bootstrap dbc.Buttons with different styles

Here are some of the options to customize the dbc.Button component.  See more examples in the [Dash Boostrap Components](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/button/)
documentation.


![buttons-style](https://user-images.githubusercontent.com/72614349/191831138-bf202640-b227-4251-81b9-cde8241313fd.png)

```python
from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

buttons = html.Div(
    [
        dbc.Button("Regular", className="me-1"),
        dbc.Button("Outline", outline=True, color="primary", className="me-1"),
        dbc.Button("Disabled", disabled=True, className="me-1"),
        dbc.Button("Large", size="lg", className="me-1"),
        dbc.Button("Small", size="sm", className="me-1"),
        dbc.Button("Link", color="link"),

    ], className= "m-4"
)

app.layout = dbc.Container(buttons)

if __name__ == "__main__":
    app.run_server(debug=True)
```



## Dash Bootstrap dbc.Button with Icons

You can add Bootstrap and/or Font Awesome icons to your Dash Bootstrap components. To learn more, see the [Icons section](https://dash-bootstrap-components.opensource.faculty.ai/docs/icons/)
of the dbc docs.

Here is an example app:

![buttons-icons](https://user-images.githubusercontent.com/72614349/192217444-c5d7d1f9-ccaa-4c80-89e9-7b68cf52a8f7.png)


```python

from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME, dbc.icons.BOOTSTRAP])

FA_icon = html.I(className="fa-solid fa-cloud-arrow-down me-2")
FA_button =  dbc.Button([FA_icon, "Download"], className="me-2")

BS_icon = html.I(className="bi bi-cloud-arrow-down-fill me-2")
BS_button = dbc.Button([BS_icon, "Download"])

app.layout = dbc.Container([FA_button, BS_button])

if __name__ == "__main__":
    app.run_server(debug=True)

```



## Dash Bootstrap dbc.Button with Dash Iconify

Another way to add icons to Dash components is to use the [Dash Iconify](https://www.dash-mantine-components.com/dash-iconify) library. 
Dash Iconify gives you access to over 100,000 free icons.  Browse the icon sets [here](https://icon-sets.iconify.design/).  

You can also specify the color, size, rotation, flip, style and more.  See the props available in [Dash Iconify GitHub.](https://github.com/snehilvj/dash-iconify) 

You can find lots of examples of components with Dash Iconify in the `dash-mantine-coponents` [documentation](https://www.dash-mantine-components.com/),
but you can also use these icons with any dash component, including `dash-bootstrap-components`. Here is an example:


![dash-iconify](https://user-images.githubusercontent.com/72614349/192217095-556e216b-c738-4278-9afe-4c6c56d165e0.png)


```python

from dash import Dash
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

download_icon = DashIconify(icon="bi:cloud-download", style={"marginRight": 5})
download_button =  dbc.Button([download_icon, "Download"], className="me-2")

settings_icon = DashIconify(icon="carbon:settings-check", style={"marginRight": 5})
settings_button = dbc.Button([settings_icon, "Settings"])

app.layout = dbc.Container([download_button, settings_button])

if __name__ == "__main__":
    app.run_server(debug=True)

```



## Dash Mantine Components dmc.Button

This app uses a button from the `dash-mantine-components` library.  You will see that the buttons are styled with fonts and colors
and design from the Mantine Themes.  As with the `dash-boostrap-components`, you can customize the style in many ways.
See the [Dash Mantine Components Documentation](https://www.dash-mantine-components.com/components/button) to see a lot more options.

![dmcButton](https://user-images.githubusercontent.com/72614349/192216440-6e8a5101-3423-40ff-870c-35b9f35061e0.png)


```python
from dash import Dash
import dash_mantine_components as dmc
from dash_iconify import DashIconify

app = Dash(__name__)

buttons = dmc.Group(
    [
        dmc.Button("Default"),
        dmc.Button("Subtle", variant="subtle"),
        dmc.Button("Gradient", variant="gradient"),
        dmc.Button("Light", variant="light"),
        dmc.Button("Outline", variant="outline"),
        dmc.Button("Radius- lg", radius="lg"),
        dmc.Button("Compact", compact=True),
        dmc.Button("Icon", leftIcon=[DashIconify(icon="fluent:settings-32-regular")],
        ),
    ]
)

app.layout = dmc.Container(buttons)

if __name__ == "__main__":
    app.run_server(debug=True)


```


## Plotly Dash App - Input and button side-by-side


![button-input-side-by-side](https://user-images.githubusercontent.com/72614349/191951955-4d49a0f0-802d-45ec-9138-c285a56c9cb3.png)

To pace the button next to the `dbc.Input`, use the `dbc.Row` and `dbc.Col` components.

```python

from dash import Dash
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.PULSE])

form = dbc.FormFloating(
    [
        dbc.Input(id="username"),
        dbc.Label("Enter username"),
    ],
)
button = dbc.Button("Submit")


app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col(form, width=4), dbc.Col(button, width="auto")])
    ], fluid=True
)


if __name__ == "__main__":
    app.run_server(debug=True)

```

## Plotly Dash App - Form with a button

In this app, a user can submit a form by clicking on the button.  The callbacks make this app interactive.


![button-form](https://user-images.githubusercontent.com/72614349/191821247-bcdb9001-a8d3-4bfb-b658-e091caed8601.gif)

```python
from dash import Dash, html, Input, Output, State
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.PULSE])

form = dbc.FormFloating(
    [
        dbc.Input(id="username"),
        dbc.Label("Enter username"),
    ]
)
button = dbc.Button("Submit")
output_container = html.Div(className="mt-4")

app.layout = dbc.Container([form, button, output_container], fluid=True)


@app.callback(
    Output(output_container, "children"),
    Input(button, "n_clicks"),
    State("username", "value"),
    prevent_initial_call=True,
)
def greet(_, name):
    return f"Welcome {name}!" if name else "Please enter username"


if __name__ == "__main__":
    app.run_server(debug=True)

```

## Plotly Dash Example Index

See more examples of interactive apps with buttons in the [Dash Example Index](https://dash-example-index.herokuapp.com/?code=button)

![Example Index](https://user-images.githubusercontent.com/72614349/192155573-39042b8f-0c54-479d-bd96-fa0eb3b96f06.png)




## Reference


### [Dash documentation - tutorial](https://dash.plotly.com/).  Getting Started with Dash

### [Dash Example Index](https://dash-example-index.herokuapp.com/?code=button).  Sample apps with buttons

### [Dash documentation](https://dash.plotly.com/dash-html-components/button). html.Button

### [Dash Bootstrap Components documentation](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/button/) - dbc.Button

### [Dash Mantine Components Documentation](https://www.dash-mantine-components.com/components/button) - dmc.Button

### [Dash Iconify](https://github.com/snehilvj/dash-iconify) - Adding Icons to Dash components

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


