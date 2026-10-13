2026-09-28 04:01

Status: #baby

Tags: [[SVG Authoring and Optimization]]

# SVG Viewport and Canvas

The SVG viewport is the rectangular region allocated by the containing document or by width and height attributes. The SVG canvas is the broader coordinate space in which elements can be defined, including regions outside the visible viewport.

Changing the viewport changes the display area; it does not by itself redefine the internal geometry. The `viewBox` supplies the mapping between a chosen internal rectangle and that viewport. See [[SVG viewBox Scaling]].

The root viewport comes from the embedding context or the SVG's width and height, while a nested `svg`, reused `symbol`, marker, pattern, or other effect can establish another viewport and coordinate system. Overflow rules determine whether content outside a viewport remains visible or is clipped. Explicit intrinsic dimensions plus a matching viewBox ratio give embedding code a predictable default size while retaining responsive scaling.

# References

[[highperformanceimages.pdf]]
[[usingsvgwithcss3andhtml5.pdf]]
