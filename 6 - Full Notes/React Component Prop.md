2026-09-06 20:52

Status: #baby

Tags: [[React Component Architecture]]

# React Component Prop

A React component prop is an input passed from a consuming component to a child component. Props make a component configurable in the same way that function parameters make a function reusable.

TypeScript interfaces can specify prop names and types, including callback functions. A component reads its props when rendering but does not treat them as its own mutable state.

Props carry data down the component tree and callback functions back toward the component that owns a change. The source treats incoming props as immutable inputs: a presentation component renders them and reports interaction through a callback rather than rewriting the supplied values.

# References

[[aspnetcore3andreact.pdf]]

[[learningreact1.pdf]]
