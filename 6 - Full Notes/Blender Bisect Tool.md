2026-09-14 01:18

Status: #baby

Tags: [[Blender Mesh Modeling and Modifiers]]

# Blender Bisect Tool

The Bisect tool cuts selected mesh geometry with a user-defined plane. It can retain both sides, clear one side, and optionally fill the cut, making it useful for trimming a model or producing a clean planar division.

Unlike a freehand knife cut, the operation is governed by one infinite plane. Plane position, orientation, clear direction, and fill state remain the key settings to inspect immediately after the cut.

In Blender 2.80, Plane Point locates the cutting plane and Plane Normal controls its direction. Fill connects newly created boundary vertices into a face, while Clear Inner and Clear Outer remove geometry on the corresponding side. Because the plane acts across the selected mesh rather than only a drawn path on visible faces, it provides a more global division than the Knife tool.

# References

[[creatinggameenvironmentsinblender3d.pdf]]

[[modelingandanimationusingblender.pdf]]
