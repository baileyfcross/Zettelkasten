2026-09-28 20:13

Status: #baby

Tags: [[Blender Render Optimization and Compositing]]

# Render Border Region Testing

A render border restricts rendering to a rectangular part of the active camera view. It lets an artist test a changed object, material, or light without paying to recompute the rest of the image.

The border is a diagnostic scope, not a crop decision for the final composition. It should be cleared when full-frame output is required, and the render settings must have border rendering enabled for the viewport rectangle to constrain the result.

# References

[[howtocheatinblender27x.pdf]]
