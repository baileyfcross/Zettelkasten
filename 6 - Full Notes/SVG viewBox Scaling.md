2026-09-28 04:01

Status: #baby

Tags: [[SVG Authoring and Optimization]]

# SVG viewBox Scaling

The SVG `viewBox` names an internal rectangle using minimum x, minimum y, width, and height. The browser maps that rectangle into the element’s viewport, scaling or shifting the drawing as needed.

A smaller viewBox can act like a zoom into part of the canvas, while changing its origin pans the selected region. Supplying a meaningful viewBox is what allows the same geometry to scale responsively rather than remaining tied to fixed width and height coordinates.

# References

[[highperformanceimages.pdf]]
