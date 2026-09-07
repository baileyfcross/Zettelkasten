2026-09-06 20:52

Status: #baby

Tags: [[React Component Architecture]]

# React Rendering

React rendering evaluates a component to produce the element tree for its current props and state. A state change rerenders the component and ordinarily its children so React can update the browser output.

Rerendering is not identical to replacing the entire document. React applies the required changes, and memoization can prevent an unchanged child from being evaluated unnecessarily when its props remain equivalent.

# References

[[aspnetcore3andreact.pdf]]
