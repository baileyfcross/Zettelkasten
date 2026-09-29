2026-09-28 04:01

Status: #baby

Tags: [[SVG Authoring and Optimization]]

# SVG Grouping and Transform Reuse

SVG groups let several elements share transforms and presentation attributes. A transform applied once to a group can replace repeated coordinate changes on every child, and reusable definitions can be referenced from multiple visible instances.

Grouping can therefore improve both structure and byte efficiency. It should reflect genuine reuse or shared behavior; deeply nested groups with inherited attributes can add complexity that makes optimization and rendering harder. See [[SVG Complexity Reduction]].

# References

[[highperformanceimages.pdf]]
