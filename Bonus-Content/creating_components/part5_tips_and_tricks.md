## Part 5 Tips & Tricks


### Testing


Prior to using a new component in a production environment, it's a best practice to create tests, especially if it's a complex component or a component library.  The [dash-component-boilerplate](https://github.com/plotly/dash-component-boilerplate) creates a simple integration test for the sample component. To start, you can modify that test to use with your own component. 


To learn more about testing in dash see:


1. The Dash Documentation section on [Testing](https://dash.plotly.com/testing).
2. The [dash-core-components tests](https://github.com/plotly/dash/tree/dev/components/dash-core-components/tests)
3. The [dash-table tests](https://github.com/plotly/dash/tree/dev/components/dash-table/tests)
4. To see how to create tests that use [Selenium](https://www.selenium.dev/), see the [pull request to add tests](https://github.com/plotly/dash-ag-grid/pull/33) to the open source version of dash-ag-grid.




### Creating Dash components with TypeScript
If you are using TypeScript, you can use the [dash-typescript-component-template](https://github.com/plotly/dash-typescript-component-template). For examples of components using TypeScript,  see [dash-mantine-component](https://github.com/snehilvj/dash-mantine-components) version >=0.11.0.


### Class vs Function
The dash-component-boilerplate creates a class component.  To see how to convert to functions see:


1. Article on [class vs functional components.](https://www.educative.io/blog/react-component-class-vs-functional)
2. React docs on [converting from class to functional](https://beta.reactjs.org/reference/react/Component#alternatives) components.
3. To see examples of converting Dash components from classes to functions, check out the [dash-bootstrap-components](https://github.com/facultyai/dash-bootstrap-components/tree/main/src/components) library. The components were refactored to use functions and hooks in 2020.  If you look at the git history, you can see the before and after and it makes it really easy to see how to make the components both ways. See for example the conversion for the [dbc.Alert component.](https://github.com/facultyai/dash-bootstrap-components/commit/728f1d5fa4ae78e0f8e23dd4c96fee545583cef8#diff-41547f5f675317d6e063e7cfe0b6c83c35326130c21b7de0de6216ac03a31488)


### Start Over at [Part 1 Getting Started](https://github.com/DashBookProject/Plotly-Dash/blob/master/Bonus-Content/creating_components/part1_getting_started.md#writing-custom-dash-components)



