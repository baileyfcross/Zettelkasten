2026-09-28 04:01

Status: #baby

Tags: [[Adaptive Image Delivery and Caching]]

# Viewport-Width Client Hint

The Viewport-Width hint communicates the width of the client’s layout viewport in CSS pixels. An image service can use it to place the request into a coarse responsive breakpoint when markup does not enumerate candidates.

Viewport width alone does not reveal the actual image slot or required physical pixels. Layout can allocate only part of the viewport, and device density changes the sample requirement. It should therefore be combined with resource width or a conservative layout model. See [[Resource Width Client Hint]].

# References

[[highperformanceimages.pdf]]
