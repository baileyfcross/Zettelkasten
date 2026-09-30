2026-09-30 00:32

Status: #baby

Tags: [[React Testing Practice]]

# React Component Test

A React component test renders a component with controlled props, inspects the resulting structure, and simulates relevant interactions. The test can assert element classes, text, child props, and callback calls without deploying the full application in a real browser.

Jest's simulated DOM supplies browser-like APIs in Node.js, while [[Enzyme Component Rendering|Enzyme]] historically provided component rendering and traversal in the source. The chosen rendering depth should match the boundary: shallow output isolates one component, whereas a mounted tree is appropriate when lifecycle and descendants are part of the behavior.

# References

[[learningreact1.pdf]]
