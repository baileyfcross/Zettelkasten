2026-09-28 04:01

Status: #baby

Tags: [[SVG Authoring and Optimization]]

# SVG Coordinate Grid

SVG places geometry in a two-dimensional coordinate system whose origin is normally at the upper-left, with x increasing to the right and y increasing downward. Shape positions and path commands are expressed in these user units.

The grid is internal to the document and need not equal device pixels. Its relationship to the displayed rectangle is established through the viewport and `viewBox`, which lets one geometric description scale to many output sizes. See [[SVG Viewport and Canvas]].

Unitless coordinate values are user units and behave like `px` within the current coordinate system, but transforms and viewBox mapping can make one user unit cover a different number of output pixels. Percentage geometry is contextual: horizontal values generally use viewport width, vertical values use height, and other distance-like values may use the normalized diagonal. Nested SVG elements can establish new grids inside the outer one.

# References

[[highperformanceimages.pdf]]
[[usingsvgwithcss3andhtml5.pdf]]
