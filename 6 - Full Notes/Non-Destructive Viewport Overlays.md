2026-09-08 09:04

Status: #baby

Tags: [[Blender Viewport Drawing API]]

# Non-Destructive Viewport Overlays

A viewport overlay presents derived information without modifying the model it describes. Object names, vertex indices, lines, and distances can be drawn each frame from current scene coordinates, leaving the mesh and renderable scene unchanged.

This separation is useful for measurement and diagnostics. The overlay can disappear when its handler is removed, while the underlying data remains intact. It also avoids creating helper geometry that might be exported or rendered accidentally, making the drawing a view-layer concern rather than part of the asset.

# References

[[blenderpythonapi.pdf]]
