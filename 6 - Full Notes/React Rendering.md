2026-09-06 20:52

Status: #baby

Tags: [[React Component Lifecycle and Integration]]

# React Rendering

React rendering evaluates a component to produce the element tree for its current props and state. A state change rerenders the component and ordinarily its children so React can update the browser output.

Rerendering is not identical to replacing the entire document. React applies the required changes, and memoization can prevent an unchanged child from being evaluated unnecessarily when its props remain equivalent.

In the source's ReactDOM example, the desired element tree and a target DOM node are passed to the renderer. React leaves existing DOM in place where possible and applies only the insertions or updates needed to make the target match the new [[Virtual DOM|virtual tree]].

# References

[[aspnetcore3andreact.pdf]]

[[learningreact1.pdf]]
