2026-09-08 09:04

Status: #baby

Tags: [[Blender Add-On Development Workflow]]

# Algorithmic Primitive Manipulation

Algorithmic primitive manipulation creates a model by applying operations such as subdivision, selection, translation, and extrusion to a simple starting shape. The procedure itself becomes the model description, so changing parameters can generate a family of related forms.

This approach is natural when parameterization is the goal, as with a maze, fence, or architectural element whose dimensions and repetitions vary. It is inefficient when a highly detailed asset is effectively fixed and only needs simple resizing; in that case, loading an interchange file preserves detail with much less code.

# References

[[blenderpythonapi.pdf]]
