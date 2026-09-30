2026-09-30 00:32

Status: #baby

Tags: [[React Routing and Forms]]

# React Hash Router

A React hash router stores the client route after `#` in the browser location. Changing or refreshing that fragment does not request a different resource path from the server, allowing a purely client-hosted single-page application to select views without server route configuration.

The source recommends the historical `HashRouter` for small client-only applications and contrasts it with browser-history routing used for universal rendering. Hash routing simplifies hosting, but the fragment becomes part of every navigable URL.

# References

[[learningreact1.pdf]]
