2026-09-30 00:32

Status: #baby

Tags: [[Universal React Applications]]

# Universal React Routing

Universal React routing selects equivalent component content from a URL on the server and from browser history on the client. The server receives the requested path, renders through a [[React Static Router|static router]], and returns the matching HTML; the browser router then owns navigation after startup.

A real path-based browser router is required when refreshing or directly opening a route should send that route to the server. Unlike a [[React Hash Router|hash router]], the path is part of the HTTP request and therefore gives server rendering the location it needs.

# References

[[learningreact1.pdf]]
