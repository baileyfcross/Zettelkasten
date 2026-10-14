2026-09-06 20:52

Status: #baby

Tags: [[React Routing and Forms]]

# Route Redirect

A route redirect replaces one client location with another. It is useful for assigning a canonical starting route, preserving an old route, or moving the user after authentication or successful form submission.

The redirect changes navigation state rather than rendering the destination page inside the old route. React Router then matches the new location to its declared component.

The source uses redirects to preserve old bookmarks after content moves into a nested route. A request for a former top-level path is translated to its canonical subsection path before the route switch selects the destination component.

# References

[[aspnetcore3andreact.pdf]]

[[learningreact1.pdf]]
