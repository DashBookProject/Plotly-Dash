# Plotly Dash Slider Components

Welcome to the bonus content of "The Book of Dash".  Here you will find additional examples of Plotly Dash components,
layouts and style.  To learn more about making dashboards with Plotly Dash, and how to buy your copy of
"The Book of Dash", please see the reference section at the bottom of this article.

This article will focus on the `dcc.Slider` and the `dcc.RangeSlider` components.  A slider is a way for users to select numeric input
between a minimum and maximum value.

## Plotly Dash dcc.Slider

Here is a minimal Dash app with a `dcc.Slider` component. 


![slider](https://user-images.githubusercontent.com/72614349/189489026-ef78466d-142f-45a2-abfb-3def0275cfca.png)

```python
from dash import Dash, dcc, html

app = Dash(__name__)

slider = dcc.Slider(min=0, max=20, step=5, value=10)

app.layout = html.Div(slider, style={"margin": 30})

if __name__ == "__main__":
    app.run(debug=True)
```


In the app above, the slider is defined as:
```python
slider = dcc.Slider(min=0, max=20, step=5, value=10)
```
Rather than using keyword arguments for the `min`, `max` and `step`, you could use positional arguments:
```python
slider = dcc.Slider(0, 20, 5, value=10)
```


## Plotly Dash dcc.RangeSlider

The `dcc.RangeSlider` component allows the user to select a range of values between the min and the max values.


![RangeSlider](https://user-images.githubusercontent.com/72614349/189491972-461baace-0adb-4955-8ced-0946a305bf90.png)


```python
slider = dcc.RangeSlider(0, 20, 2, value=[6, 16])
```


## Plotly Dash dcc.Slider with a Label


![slider with a label](https://user-images.githubusercontent.com/72614349/189503968-33d14a4c-ebd7-4175-9a41-d974a52537a0.png)

It's commonn to add a label with an `html.Div` component, however  if you use an `html.Label` (or `dbc.Label` with
`dash-bootstrap-components`), there are several advantages:

From [Mozilla mdn Web Docs:](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label)

> - The label text is not only visually associated with its corresponding text input; it is programmatically associated 
> with it too. This means that, for example, a screen reader will read out the label when the user is focused on the form
> input, making it easier for an assistive technology user to understand what data should be entered.
> - When a user clicks or touches/taps a label, the browser passes the focus to its associated input (the resulting
> event is also raised for the input). That increased hit area for focusing the input provides an advantage to
> anyone trying to activate it — including those using a touch-screen device.

In the example below, note that the html.Label must include the `htmlFor` prop which uses the same id as the slider.  

```python

slider = html.Div(
    [
        html.Label("Select Number", htmlFor="my-slider"),
        dcc.Slider(min=0, max=20, step=5, value=10, id="my-slider")
    ]
)
```

## Plotly Dash Sliders with Marks

You can put marks (ie labels) along the slider rail. For example:


![slider with marks](https://user-images.githubusercontent.com/72614349/189503727-cdb24672-2a37-45e0-8878-260fc7ff91a2.png)


## Plotly Dash Sliders with Marks
```
slider = dcc.Slider(
    1, 12, 3, value=6, marks={1: "Jan", 3: "Mar", 6: "Jun", 9: "Sep", 12: "Dec"}
)
```

## Plotly Dash Sliders with marks at an angle

You can customize each mark with css using the `style` prop. This slider has the marks displayed on a 45-degree angle
to make them more readable on small screens or narrow columns. See the dash docs for more examples of customizing
and styling the marks.

![slider marks 45deg](https://user-images.githubusercontent.com/72614349/189503760-5c765dfa-c232-4852-bfbe-9a89075cd0e8.png)


```python

slider = dcc.RangeSlider(1, 12, 1, value=[3, 9],
    marks={
        i: {
            "label": f"Month {i}",
            "style": {"transform": "rotate(45deg)", "white-space": "nowrap"},
        }
        for i in range(1, 13)
    },
)
```


## Plotly Dash dcc.Slider with a Bootstrap theme

If you are using `dash-bootstrap-components`, you will notice that Bootstrap theme is not automatically applied to 
`dash-core-components` such as the `dcc.Slider`  However, a co-author of "The Book of Dash" has developed a stylesheet
that will update the `dcc` components with colors and fonts of your selected Bootstrap theme. Simply include this
stylesheet and add `className="dbc"` to your app.  Here are some examples:

#### `dcc.Slider` with a Bootstrap Pulse Theme
![dcc.Slider with Pulse Theme](https://user-images.githubusercontent.com/72614349/189487800-a5e9688c-0337-4346-8f52-1216cb101bb9.png)

#### `dcc.Slider` with a Bootstrap Cyborg Theme
![dcc.Slider with a Cyborg theme](https://user-images.githubusercontent.com/72614349/189487989-9a0b2975-93e8-478f-b470-9bca39d35723.png)


```python
from dash import Dash, dcc
import dash_bootstrap_components as dbc

# stylesheet with the .dbc class from dash-bootstrap-templates library
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

# Bootstrap Pulse theme
app = Dash(__name__, external_stylesheets=[dbc.themes.PULSE, dbc_css])  

# Bootstrap Cyborg theme
# app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG, dbc_css]) 

slider = dcc.Slider(min=0, max=20, step=5, value=10, className="m-4")

app.layout = dbc.Container([slider], fluid=True, className="dbc")

if __name__ == "__main__":
    app.run(debug=True)

```

## Display Two Sliders Side-by-Side

One of the easiest ways to design your app's layout is to use the stylesheets from libraries such as
`dash-bootstrap-components` or `dash-mantine-components`.  In this example we place the sliders in
one row and two columns using the `dbc.Row()` and `dbc.Col()` components.

![Two sliders side by side](https://user-images.githubusercontent.com/72614349/189492433-f8b9a2d1-f5ea-4d4a-b6a6-0d32d66823bf.png)

```python

from dash import Dash, dcc
import dash_bootstrap_components as dbc

# stylesheet with the .dbc class from dash-bootstrap-templates library
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

app = Dash(__name__, external_stylesheets=[dbc.themes.MINTY, dbc_css])

slider = dcc.Slider(min=0, max=20, step=5, value=10, className="m-4")
range_slider = dcc.RangeSlider(0, 20, 2, value=[6, 16], className="m-4")

app.layout = dbc.Container(
    [dbc.Row([dbc.Col(slider), dbc.Col(range_slider)])], fluid=True, className="dbc"
)

if __name__ == "__main__":
    app.run(debug=True)
```

## Plotly Dash App - Updating a figure with a dcc.Slider

In this app, a user can update the figure by selecting the year on the slider.  The callbacks make this app interactive.
This example also shows how to use a tooltip to display the selected value of the slider.

See more apps in the [Dash Example Index](https://dash-example-index.herokuapp.com/?code=slider)


![graph and a slider](https://user-images.githubusercontent.com/72614349/189505097-2ee83a75-38b2-435f-bfa9-4ce802a90ce3.png)


```python
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = px.data.gapminder()
years = df.year.unique()

app = Dash(__name__)

slider = html.Div(
    [
        html.Label("Select Year", htmlFor="years"),
        dcc.Slider(
            min=years[0],
            max=years[-1],
            step=5,
            value=years[0],
            id="years",
            marks=None,
            tooltip={"placement": "bottom", "always_visible": True},
        ),
    ]
)

app.layout = html.Div([slider, dcc.Graph(id="graph")])


@app.callback(Output("graph", "figure"), Input("years", "value"))
def update_figure(yr):
    return px.scatter(
        df.query(f"year=={yr}"),
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        log_x=True,
        size_max=60,
        title=f"{yr} Life Expectancy vs GDP Per Capita",
    )


if __name__ == "__main__":
    app.run(debug=True)

```

## Reference

### [Order Your Copy of "The Book of Dash" Today!](https://nostarch.com/book-dash)
![The Book Of Dash](https://user-images.githubusercontent.com/72614349/185497519-733bdfc3-5731-4419-9a68-44c1cad04a78.png)



### [Dash documentation - tutorial](https://dash.plotly.com/).  Getting Started with Dash

### [Dash Example Index](https://dash-example-index.herokuapp.com/?code=slider).  Sample apps with sliders

### [Dash documentation - dcc.Slider](https://dash.plotly.com/dash-core-components/slider)

### [Dash Bootstrap Components documentation - Themes](https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/)

### [Dash Bootstrap Theme Explorer](https://hellodash.pythonanywhere.com/). A guide for styling Plotly Dash apps with a Bootstrap theme



