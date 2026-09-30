2026-09-06 20:52

Status: #baby

Tags: [[React Routing and Forms]]

# React Link

A React Router Link renders navigable content that changes the client-side location without forcing a full document request. It preserves browser navigation behavior while letting the router select the destination component.

Links are appropriate when navigation is part of rendered content. An event handler that decides a destination after work completes can use [[Programmatic Navigation]] instead.

The source also uses the historical `NavLink` variant for menus whose styling depends on whether the destination matches the current location. The link remains a navigation declaration, while the router controls which component appears after the location changes.

# References

[[aspnetcore3andreact.pdf]]

[[learningreact1.pdf]]
