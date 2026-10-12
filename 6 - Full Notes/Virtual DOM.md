2026-09-30 00:32

Status: #baby

Tags: [[React Component Architecture]]

# Virtual DOM

The virtual DOM is React's in-memory tree of [[React Element|React elements]] describing the interface that should exist. Application code changes JavaScript data and produces a new element description instead of issuing a sequence of direct browser DOM mutations.

React compares the desired tree with the prior rendering and uses the browser DOM API to apply the required changes. The abstraction does not eliminate DOM work; it moves the bookkeeping and update strategy into [[ReactDOM]] so components can describe output declaratively.

# References

[[learningreact1.pdf]]
