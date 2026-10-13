2026-09-28 04:01

Status: #baby

Tags: [[SVG Authoring and Optimization]]

# SVG Filter Primitive Pipeline

SVG filters build effects by passing image inputs through primitives such as blurs, color operations, offsets, composites, and merges. Each primitive can consume a source or an earlier intermediate result and assign output for later stages.

This graph permits sophisticated scalable effects, but every stage expands work beyond simple shape painting. Filter regions and resolution should be bounded carefully because large blurs or unnecessary intermediates increase processing cost even when the SVG text itself is small.

Each primitive can read the source graphic, source alpha, a named earlier result, or other defined inputs, and operations such as merge or composite combine branches of the graph. The filter region also clips the result, so blur, offset, or morphology may disappear at the edges unless the region includes their expansion. Since the pipeline repeatedly rasterizes and manipulates pixels at render time, animating a filtered source can multiply the cost.

# References

[[highperformanceimages.pdf]]
[[usingsvgwithcss3andhtml5.pdf]]
