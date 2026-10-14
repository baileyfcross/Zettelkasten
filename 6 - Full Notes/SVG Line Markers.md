2026-10-12 23:34

Status: #baby

Tags: [[SVG Authoring and Optimization]]

# SVG Line Markers

An SVG `marker` defines a reusable decoration that the renderer positions at the start, intermediate vertices, or end of a path-like shape. `marker-start`, `marker-mid`, and `marker-end` reference the definition; the `marker` shorthand assigns the same marker to every supported position. Arrowheads and repeated data-point symbols are common applications.

The marker has its own coordinate system. Its reference point aligns with the marked vertex, `orient="auto"` rotates its x-axis to follow the path tangent, and `markerUnits` chooses whether its size scales with the target's [[SVG Stroke Geometry|stroke width]] or remains in user-space units. A closed path can place start and end markers at the same location.

Markers are decorations of the host shape, not independent instances for events, titles, or accessibility. A chart that needs each point to be focusable or clickable should draw separate elements, such as `use` instances, instead. This distinction also means marker graphics do not independently participate in [[SVG Pointer Event Hit Testing]].

# References

[[usingsvgwithcss3andhtml5.pdf]]

