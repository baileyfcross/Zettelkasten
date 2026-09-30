2026-09-06 20:52

Status: #baby

Tags: [[React Routing and Forms]]

# Route Parameter

A route parameter is a variable segment embedded in a route path, such as the identifier in a question URL. When a location matches, React Router supplies the captured text to the rendered component.

The component converts and validates the value before using it to fetch a resource. An effect that depends on the parameter reruns when navigation changes that value without replacing the component type.

The source declares a parameter with a colon-prefixed path segment and reads the captured value from `match.params`. Multiple segments can be captured, and a connected component can use the resulting identifier to select one record from Redux state.

# References

[[aspnetcore3andreact.pdf]]

[[learningreact1.pdf]]
