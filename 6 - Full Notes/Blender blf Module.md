2026-09-08 09:04

Status: #baby

Tags: [[Blender Viewport Drawing API]]

# Blender blf Module

The `blf` module draws text in Blender. A drawing function selects a font identifier and size, positions the text in two-dimensional viewport coordinates, and supplies the string to display.

Text is commonly paired with line drawing to label object names, vertex indices, or measurements. Like other viewport drawing, the result exists for only a frame and must be produced again by a draw callback. This transient behavior makes the label an informational overlay rather than a text mesh stored in the scene.

# References

[[blenderpythonapi.pdf]]
