2026-09-30 00:32

Status: #baby

Tags: [[React Component Architecture]]

# ReactDOM

ReactDOM is the platform adapter that renders React elements into a browser document. Its `render` operation receives an element tree and a target DOM node, then inserts or updates the browser elements needed to make that target reflect the current tree.

Separating React's element and component model from ReactDOM's browser operations allows the same component descriptions to target other environments. The source's React 15 API also places server string-rendering operations in the ReactDOM family, supporting [[React Server Rendering]].

# References

[[learningreact1.pdf]]
