2026-09-06 20:52

Status: #baby

Tags: [[React Routing and Forms]]

# Route Declaration

A route declaration associates a URL path pattern with the React component that should render for it. A collection of declarations forms the navigable structure of the client application.

Ordering and exact matching matter because a broad path may otherwise match before a more specific one. Parameter segments allow one declaration to represent many resource-specific locations.

In the source's React Router version, a `Route` supplies `path` and `component` props inside a router. A `Switch` renders only the first matching route, while routes outside a switch may deliberately render together, as with a persistent submenu and one nested content route.

# References

[[aspnetcore3andreact.pdf]]

[[learningreact1.pdf]]
