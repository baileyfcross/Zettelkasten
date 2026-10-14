2026-09-28 04:01

Status: #baby

Tags: [[SVG Authoring and Optimization]]

# SVG Shape Primitives

SVG provides declarative primitives such as rectangles, circles, ellipses, lines, polylines, and polygons. Their geometry is represented with compact attributes rather than a grid of pixels.

Using the simplest adequate primitive improves readability and can reduce source size. More irregular contours use paths, but converting every basic shape into verbose path data can sacrifice semantic clarity without a useful performance gain. See [[SVG Path Command Economy]].

The standard geometric elements are deliberately few: rectangle, circle, ellipse, and line cover frequent cases, while polygon, polyline, and path cover arbitrary contours. Their attributes accept numbers, lengths, and context-dependent percentages. This makes primitives independently adjustable and easy to query or animate, whereas a converted path hides the same geometry inside one command string.

# References

[[highperformanceimages.pdf]]
[[usingsvgwithcss3andhtml5.pdf]]
