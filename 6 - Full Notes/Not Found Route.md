2026-09-06 20:52

Status: #baby

Tags: [[React Routing and Forms]]

# Not Found Route

A not-found route is the fallback client route rendered when no declared path matches the current location. It gives the user an intentional explanation and navigation path instead of an empty interface.

The fallback must be ordered after the specific route declarations. It handles unknown client locations, while a missing REST resource still requires an appropriate server [[HTTP Status Code]].

A first-match switch makes the pathless fallback safe: every known route appears before it, and the fallback renders only when none matches. The router's [[React Router Location Prop|location prop]] can then include the unmatched pathname in the explanation shown to the user.

# References

[[aspnetcore3andreact.pdf]]

[[learningreact1.pdf]]
