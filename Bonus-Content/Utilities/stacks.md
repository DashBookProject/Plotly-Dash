# Plotly Dash App Layouts  using Bootstrap Stacks

### Welcome to the bonus content of "The Book of Dash".  :hugs:

Here you will find additional examples of Plotly Dash components, layouts and style.  To learn more about making
dashboards with Plotly Dash, and how to buy your copy of ["The Book of Dash"](https://nostarch.com/book-dash), please see the reference section
at the bottom of this article.

This article covers Bootstrap Stacks utility class  -- the Bootstrap shorthand helper to make component layout faster and
easier than ever.  The examples are adapted for Plotly Dash apps from the official [Bootstrap documentation.](https://getbootstrap.com/docs/5.2/helpers/stacks/)


## Dash Bootstrap utility classes

Bootstrap includes dozens of utility classes for showing, hiding, aligning, spacing and styling content.
Bootstrap utility classes can be applied to any Dash component to quickly style them without the need to write custom 
CSS rules. Use the  Bootstrap utility classes in the Dash component's  `className` prop.  

See all the Bootstrap classes  at the [Dash Bootstrap Cheatsheet](https://dashcheatsheet.pythonanywhere.com/) app. 
This handy cheatsheet is made by a co-author of “The Book of Dash”.

Feel free to watch Adam’s explainer [video](https://www.youtube.com/watch?v=vqVwpL4bGKY&t=16s) on Bootstrap and styling 
your app if you need to get up to speed! 

### Vertical Layouts 

Use `"vstack"` in the `className` prop to create vertical layouts.  Stacked items are full-width by default.  Use the `"gap-*"`
utilities to add space between items. 

![vstack](https://user-images.githubusercontent.com/72614349/196278215-970272d5-f402-4f63-93ef-cf1c313011fc.png)


```python
from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

stack = html.Div(
    [
        html.Div("First item", className="bg-light border"),
        html.Div("Second item", className="bg-light border"),
        html.Div("Third item", className="bg-light border")
    ], className="vstack gap-3"
)

app.layout= dbc.Container(stack)

if __name__ == "__main__":
    app.run(debug=True)

```


### Dash Bootstrap Horizontal Layouts

Use `"hstack"` for horizontal layouts.  Stacked items are vertically centered by default and only take up their necessary
width.  Use the `"gap-*"` utilities to add space between items.

Here we change to a horizontal layout by changing one line of code:  Try changing from `"vstack"` to `"hstack"` in the example
app above.  

![hstack](https://user-images.githubusercontent.com/72614349/196278518-c48e397d-b287-4fe2-900b-4007842efb31.png)

```python

stack = html.Div(
    [
        html.Div("First item", className="bg-light border"),
        html.Div("Second item", className="bg-light border"),
        html.Div("Third item", className="bg-light border")
    ], className="hstack gap-3"
)
```

### Dash Bootstrap Horizontal Margins

This example uses horizontal margin utilities.  Here we use `"ms-auto"` on the second item:


![ms-auto](https://user-images.githubusercontent.com/72614349/196278842-abb4221c-34b2-45dc-b84e-17ddd6a42c9c.png)



```python

stack = html.Div(
    [
        html.Div("First item", className="bg-light border"),
        html.Div("Second item", className="bg-light border ms-auto"),
        html.Div("Third item", className="bg-light border")
    ], className="hstack gap-3"
)
```

### Dash Bootstrap Vertical Rules

The utility `"vr"` is an easy way to add a vertical line between elements.


![vr](https://user-images.githubusercontent.com/72614349/196279172-00c708c6-0c22-4ae8-8159-129af9fa6311.png)

```python

stack = html.Div(
    [
        html.Div("First item", className="bg-light border"),
        html.Div("Second item", className="bg-light border ms-auto"),
        html.Div(className="vr"),
        html.Div("Third item", className="bg-light border")
    ], className="hstack gap-3"
)
```

Use `"vstack"` to stack buttons and other elements:


![vstack-btn](https://user-images.githubusercontent.com/72614349/196279498-63c20667-172c-410f-9bad-b460577096f6.png)

```python

stack = html.Div(
    [
        dbc.Button("Save Changes", color="secondary"),
        dbc.Button("Cancel", color="secondary", outline=True),
    ],
    className="vstack gap-2 col-md-3 mx-auto",
)
```

Create an in-line form with `"hstack"`


![hstack-form](https://user-images.githubusercontent.com/72614349/196279885-b21e30d6-cddf-42f6-a9a1-90959d51d32f.png)


```python

stack = html.Div(
    [
        dbc.Input(placeholder="Add your item here...", className="me-auto"),
        dbc.Button("Submit", color="secondary"),
        html.Div(className="vr"),
        dbc.Button("Reset", color="danger", outline=True),
    ],
    className="hstack gap-3",
)

```

## Dash Bootstrap Theme Explorer

You can also find more details and examples in the Dash Bootstrap Theme Explorer [Bootstrap Utility Classes Secion](https://hellodash.pythonanywhere.com/adding-themes/bootstrap-utility-classes)
You will be able to try out different utility classes in a live demo.  Here's an example!

![ulilites live demo](https://user-images.githubusercontent.com/72614349/197416744-9b57ce8d-f300-4497-a532-78e02aa6e5a1.gif)


## Plotly Dash Example Index

See more examples of Bootstrap utility classes live!  Check out the interactive example apps in the [Dash Example Index](https://dash-example-index.herokuapp.com)

![Example Index](https://user-images.githubusercontent.com/72614349/192155573-39042b8f-0c54-479d-bd96-fa0eb3b96f06.png)





## Reference


### [Dash documentation - tutorial](https://dash.plotly.com/).  Getting Started with Dash

### [Dash Example Index](https://dash-example-index.herokuapp.com/).  Lots of sample apps to get you started with Dash!

### [Dash Bootstrap Components documentation](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/) 

### [Dash Bootstrap Cheatsheet](https://dashcheatsheet.pythonanywhere.com/) A cheatsheet for using Bootstrap utility classes with Dash

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



