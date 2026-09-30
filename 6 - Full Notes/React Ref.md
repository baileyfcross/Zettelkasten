2026-09-30 00:32

Status: #baby

Tags: [[React Component Architecture]]

# React Ref

A React ref retains access to a rendered element or component instance when declarative props and callbacks are not sufficient for an imperative interaction. The source uses refs to read and reset input values, move focus, and integrate code that needs a concrete DOM node.

Its examples use historical string refs on class components and callback refs on function components. The durable boundary is that a ref is an escape hatch to an instance; routine data flow should still use props, state, and event callbacks so the component tree remains understandable.

# References

[[learningreact1.pdf]]
