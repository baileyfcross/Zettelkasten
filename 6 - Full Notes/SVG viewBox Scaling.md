2026-09-28 04:01

Status: #baby

Tags: [[SVG Authoring and Optimization]]

# SVG viewBox Scaling

The SVG `viewBox` names an internal rectangle using minimum x, minimum y, width, and height. The browser maps that rectangle into the element’s viewport, scaling or shifting the drawing as needed.

A smaller viewBox can act like a zoom into part of the canvas, while changing its origin pans the selected region. Supplying a meaningful viewBox is what allows the same geometry to scale responsively rather than remaining tied to fixed width and height coordinates.

The viewBox also establishes an intrinsic aspect ratio from its width and height. If that ratio differs from the viewport, `preserveAspectRatio` chooses between nonuniform distortion, fitting the entire region with spare space, or filling the viewport by cropping. The mapping scales units and shifts the origin without rewriting any child coordinates.

# References

[[highperformanceimages.pdf]]
[[usingsvgwithcss3andhtml5.pdf]]
