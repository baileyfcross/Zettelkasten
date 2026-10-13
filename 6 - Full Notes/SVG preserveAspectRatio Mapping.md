2026-10-12 23:34

Status: #baby

Tags: [[SVG Authoring and Optimization]]

# SVG preserveAspectRatio Mapping

`preserveAspectRatio` controls how a [[SVG viewBox Scaling|viewBox]] is mapped into a viewport when their aspect ratios differ. It has no effect without a viewBox. The value `none` scales the x and y axes independently, filling the viewport but distorting geometry and stroke widths when the scale factors differ.

Aspect-preserving values combine an alignment token with either `meet` or `slice`. The alignment selects which minimum, middle, or maximum x and y positions coincide between the viewBox and [[SVG Viewport and Canvas|viewport]]. `meet` uses the largest uniform scale that keeps the entire viewBox visible, which may leave unused bands; `slice` uses the smallest uniform scale that fills the viewport, which may crop or overflow part of the viewBox. The default is `xMidYMid meet`.

This separates two decisions that are often conflated: how large the coordinate system becomes and which part remains visible. It is analogous to `contain` versus `cover` in CSS, but the SVG alignment token makes the anchor explicit.

# References

[[usingsvgwithcss3andhtml5.pdf]]

