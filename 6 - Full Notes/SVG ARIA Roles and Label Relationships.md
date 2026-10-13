2026-10-12 23:34

Status: #baby

Tags: [[Accessible Interactive and Animated SVG]]

# SVG ARIA Roles and Label Relationships

ARIA describes how SVG structure should appear in an accessibility tree. `role="img"` collapses an element and its descendants into one named image, while `role="group"` preserves meaningful accessible children under a labeled container. `role="presentation"` suppresses an otherwise meaningful wrapper but leaves its children available; `aria-hidden="true"` removes an entire subtree.

`aria-labelledby` can assemble an accessible name from one or more elements identified by ID. In a chart, a bar can reference a category label, series label, and value label in reading order, reusing visible text instead of duplicating it. `aria-describedby` can associate supplemental explanation, although the book reports weaker historical SVG support than for core HTML relationships.

The role determines whether descendants remain reachable, so it cannot be added mechanically. An image role on a complex interactive graphic would hide the controls that [[SVG Keyboard Focus Management|keyboard users]] need. Naming, grouping, hiding decorative duplicates, and focus behavior should therefore be designed as one semantic structure alongside [[SVG Accessible Names and Descriptions]].

# References

[[usingsvgwithcss3andhtml5.pdf]]

