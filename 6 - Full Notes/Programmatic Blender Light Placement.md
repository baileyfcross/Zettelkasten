2026-09-08 09:04

Status: #baby

Tags: [[Automated Blender Texturing and Rendering]]

# Programmatic Blender Light Placement

Programmatic lighting creates lights of a chosen type, places them relative to the modeled scene, and orients directional lights toward a target. Point, spot, area, hemispheric, and sun lights differ in how position and rotation affect illumination in the Blender version discussed by the source.

The aggregate bounding box of scene meshes provides a useful spatial reference. Lights can be distributed around its extents, while a direction vector from a light to the box center can be converted into the required rotation. This makes lighting respond to generated geometry instead of assuming fixed world coordinates.

# References

[[blenderpythonapi.pdf]]
