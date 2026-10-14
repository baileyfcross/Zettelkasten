2026-09-30 00:32

Status: #baby

Tags: [[React Testing Practice]]

# Enzyme Component Rendering

Enzyme is the historical React testing utility used by the source to render components, traverse their output, inspect props and state, and simulate events. It is a rendering and inspection layer rather than the assertion framework itself.

Its `shallow` mode renders one component level for isolation, `mount` builds a DOM-backed tree with lifecycle and descendants, and `render` produces static markup. Selecting the smallest mode that exposes the contract keeps a [[React Component Test]] focused on the intended boundary.

# References

[[learningreact1.pdf]]
