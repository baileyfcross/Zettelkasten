2026-09-06 20:52

Status: #baby

Tags: [[React Routing and Forms]]

# Programmatic Navigation

Programmatic navigation changes the client route from application logic rather than from a rendered link. A component can use router history after a button action, form submission, or authentication callback.

The destination becomes part of browser history according to the chosen operation. This keeps navigation state coordinated with the route system instead of directly replacing the page location.

The source uses the router's history prop to push a selected record's identifier as a new route and to return with `goBack`. Its historical `withRouter` wrapper supplies match, history, and location props to a descendant that was not rendered directly by a route.

# References

[[aspnetcore3andreact.pdf]]

[[learningreact1.pdf]]
