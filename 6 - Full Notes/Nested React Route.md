2026-09-30 00:32

Status: #baby

Tags: [[React Routing and Forms]]

# Nested React Route

A nested React route places route declarations inside the component for a broader section, allowing a URL hierarchy to map to a component hierarchy. A shared section menu can remain visible while a matching child route changes only the subsection content.

Nested routes need not use one global switch. When several matching elements should render together, a persistent route can supply the menu while a more specific route supplies the selected page; a switch is reserved for alternatives where only the first match should appear.

# References

[[learningreact1.pdf]]
