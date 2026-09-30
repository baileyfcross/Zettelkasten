2026-09-30 00:32

Status: #baby

Tags: [[Universal React Applications]]

# React Server Rendering

React server rendering evaluates a component tree on the server and converts it into an HTML string for the initial response. In the source's API, `renderToString` produces the markup that an Express handler places inside the page's React container.

The browser receives meaningful HTML before the client bundle renders the same application and takes over interaction. The technique can improve initial content delivery and preserve content when client JavaScript is unavailable, but it requires the server and browser to begin from compatible components, route, and state.

# References

[[learningreact1.pdf]]
