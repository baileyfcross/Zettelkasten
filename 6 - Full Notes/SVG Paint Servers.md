2026-10-12 23:34

Status: #baby

Tags: [[SVG Authoring and Optimization]]

# SVG Paint Servers

An SVG paint server is a reusable definition that supplies color across a fill or [[SVG Stroke Geometry|stroke]]. SVG 1.1 defines linear gradients, radial gradients, and tiled patterns. The painted element refers to the definition with a `url()` value, optionally followed by a solid fallback color for an unavailable, invalid, or unsupported reference.

Paint is evaluated as an independent image and then sampled wherever the target's fill or stroke region is rasterized. `userSpaceOnUse` expresses the paint geometry in the target's user coordinate system. `objectBoundingBox` instead maps a unit square onto the target's fill bounding box, which makes an effect adapt to each target but can distort it when width and height scale differently or fail when a dimension is zero.

Gradients and patterns are thus coordinate systems as well as styles. Their units, transforms, bounds, and fallback behavior must be designed together with the target's [[SVG Coordinate Grid|geometry]]. Reusing one server can centralize a visual rule, but cross-file references and bounding-box calculations require browser testing.

# References

[[usingsvgwithcss3andhtml5.pdf]]

