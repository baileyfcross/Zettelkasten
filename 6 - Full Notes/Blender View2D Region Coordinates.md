2026-09-14 00:20

Status: #baby

Tags: [[Blender Editor Construction]]

# Blender View2D Region Coordinates

`View2D` stores the scrolling, zooming, and drawable two-dimensional extents of a [[Blender Region Structure]]. In a custom main region, its mask supplies the minimum and maximum coordinates within which the draw callback can position visual elements.

The tutorial uses these bounds to inset several rectangles from the edges of the region. [[Blender Main Region Initialization]] establishes the view, while the [[Blender UI View2D API]] provides standard setup and drawing utilities that keep custom code consistent with other editors.

# References

[[coreblenderdevelopment.pdf]]

