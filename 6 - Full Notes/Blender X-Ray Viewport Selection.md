2026-10-02 18:09

Status: #baby

Tags: [[Blender 3D Viewport and Object Operations]]

# Blender X-Ray Viewport Selection

Blender's X-ray viewport option makes geometry behind visible surfaces available for inspection and selection. In mesh editing, this changes a screen-space selection from choosing only front-facing components to potentially including vertices, edges, or faces on the far side of the object.

The option should be chosen intentionally because it changes selection semantics, not just appearance. X-ray is useful when a box or lasso selection should pass through an object, while an opaque view protects hidden components from accidental editing. Its transparency value controls how strongly the interior and opposite side remain visible during the operation.

# References

[[modelingandanimationusingblender.pdf]]
