
## Part 4 Examples

### Example 1 Before and After Image slider - Convert an *Existing* React Component to Dash

This example demonstrates how to make a Dash interface to [react-before-after-slider](https://www.npmjs.com/package/react-before-after-slider) which is a component to show differences in an image like at this site:

https://jwt.pythonanywhere.com/

![webb](https://user-images.githubusercontent.com/72614349/179326884-a9a01fef-6f64-4de0-a40f-b206f3a99ff8.gif)

 Before creating your own  component,  it's always good to see if a Dash community member has already done so.  In this case, we're in luck because  you can find this component, along with several others in @Emil's [dash-extensions](https://github.com/thedirtyfew/dash-extensions/tree/master/src/lib/components) library.  You can also search the [show-and-tell](https://community.plotly.com/tag/show-and-tell) section on the Dash forum,  and the [Dash Community Components](https://plotly.com/dash-community-components/) section in the Dash documentation.  

This example will show the steps to take when creating a Dash component from an existing React component.  The important thing to know is that Dash components are mostly simple wrappers around React components. This means the entire React ecosystem is potentially usable in a Dash application.  The React community is huge. Thousands of components have been built and released with open source licenses.

To start, we can search for packages on [npm](https://www.npmjs.com/).  When you look for existing React components, you will often find several packages to choose from.  So how do you decide which one to use?  Here are some things to consider:
-  Functionality - Does the component have all the features you are looking for?
-  Documentation - High quality documentation will make development a lot easier.
-  Number of downloads  -  Popularity can be an indicator of quality.
- Bundle size, number of dependencies
-  Issues and pull requests on Github.  If a package is actively maintained then it's more likely that bugs and security issues are addressed now and in the future. 





 Let's select [react-before-after-slider](https://www.npmjs.com/package/react-before-after-slider) and go to its homepage on NPM.  Typically, you will see install instructions, sample usage, and a description of the component properties.  We will use that information to create our Dash component.


This component is very simple to use with Dash because the slider functionality is completely contained within the React component.  There is no need for Dash callbacks to make this slider interactive in an app. 



**Install**

First, install `react-before-after-slider`  according to the instructions.  This is similar to doing `pip install` with a python module.  From the root directory of the project you created with the [dash-component-boilerplate](https://github.com/plotly/dash-component-boilerplate):

```
$ npm install --save react-before-after-slider
```

**Usage**

This is the sample usage from the homepage page for `react-before-after-slider`.

```
import React, { Component } from 'react'
 
import BeforeAfterSlider from 'react-before-after-slider'
 
class Example extends Component {
  render () {
    const before = 'https://...example1.jpg'
    const after = 'https://...example2.jpg'
 
    return (
      <BeforeAfterSlider
        before={before}
        after={after}
        width={640}
        height={480}
      />
    )
  }
}
```
**Props**
You can see a list of the props available on the component's NPM homepage [here](https://www.npmjs.com/package/react-before-after-slider#props). 


**Dash Component**

Based on the usage and prop descriptions on NPM, we can create our Dash component.  We will name it  `BeforeAfter`.  Let's create a new file with the following code in the same directory as the example component `MyComponent` that was created with the Dash Component Boilerplate:

`src/lib/components/BeforeAfter.react.js`

```
import React, {Component} from 'react';
import PropTypes from 'prop-types';
import BeforeAfterSlider from 'react-before-after-slider';

/**
 * A before and after image slider based on https://www.npmjs.com/package/react-before-after-slider
 */
export default class BeforeAfter extends Component {
    render() {
        return <BeforeAfterSlider {...this.props} />;
    }
}

BeforeAfter.defaultProps = {
    width: 600,
    height: 400,
    defaultProgress: 0.5,
};

BeforeAfter.propTypes = {
    /**
     * URL of before image to use.
     */
    before: PropTypes.string.isRequired,

    /**
     * URL of after image to use.
     */
    after: PropTypes.string.isRequired,

    /**
     * Width of the image in pixels
     */
    width: PropTypes.number,

    /**
     * Height of the image in pixels
     */
    height: PropTypes.number,

    /**
     * Where the progress slider should start (float between 0 and 1).
     */
    defaultProgress: PropTypes.number,

    /**
     * Class name to add to before element.
     */
    beforeClassName: PropTypes.string,

    /**
     * Class name to add to before element.
     */
    afterClassName: PropTypes.string,
};
```


If you compare this file to  `src/lib/components/MyComponent.js` you will see many similarities.    The first two lines are the same.  The next line imports the `react-before-after-slider` component that we installed earlier as `BeforeAfterSlider`.  In the `return` statement, we send all the props to the React component.  

The rest of the code simply defines the `propTypes` and the `defaultProps`. We copied the prop names and descriptions from the [homepage](https://www.npmjs.com/package/react-before-after-slider#props).  You can see from the prop descriptions that this React component has 4 required props: the before and after images and the height and width of the image.  To make things easier in our app, we will define the width and height as  `defaultProps`, so we will only need to make the before and after images required in our Dash app.

Next add the component to the `src/lib/index.js` file:  

```
import MyComponent from './components/MyComponent.react';
import BeforeAfter from './components/BeforeAfter.react';

export {
    MyComponent,
    BeforeAfter
};
```
We now have two components in our custom-components package. Finally,  rebuild the components with:

`$ npm run build`


Your components are now ready to use in a Dash app!  Try out the new component in  `usage.py`

```
import custom_components
import dash
import dash_html_components as html


app = dash.Dash(__name__)

image1 = "https://user-images.githubusercontent.com/72614349/128639502-fc9e1ba9-1493-4f37-ab35-032f421310ca.jpeg"
image2 = "https://user-images.githubusercontent.com/72614349/128639504-61191084-a64f-4ccc-8d05-3702cc4a0e9c.jpeg"

app.layout = html.Div(custom_components.BeforeAfter(before=image1, after=image2))

if __name__ == "__main__":
    app.run_server(debug=True)

```

### Up Next [Part 5 Tips & Tricks](https://github.com/DashBookProject/Plotly-Dash/blob/master/Bonus-Content/creating_components/part5_tips_and_tricks.md#part-5-tips--tricks)
