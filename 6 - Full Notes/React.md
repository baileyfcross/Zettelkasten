2026-09-06 20:52

Status: #baby

Tags: [[React Component Architecture]]

# React

React is an open-source JavaScript library for building component-based browser interfaces. A React application expresses the visible interface as a tree of elements produced by components and rerenders affected output when component state changes.

React supplies the component and rendering model rather than a complete full-stack framework. Libraries such as [[React Router]] and [[Redux]] add routing and shared state, while an ASP.NET Core [[Web API]] can provide the back end.

The source emphasizes this small-library boundary: React creates view descriptions, while [[ReactDOM]] performs browser rendering. That separation allows the component model to be reused beyond one DOM target and leaves routing, data architecture, and server communication as explicit surrounding choices.

# References

[[aspnetcore3andreact.pdf]]

[[learningreact1.pdf]]
