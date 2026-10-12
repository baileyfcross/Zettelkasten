2026-09-14 01:18

Status: #baby

Tags: [[Blender Mesh Shaping Tools]]

# Blender Normal-Oriented Mesh Editing

Normal-oriented tools move each selected component relative to the direction its surface faces. This is different from translating an entire selection along the scene's global axes and is better suited to expanding, contracting, or extruding irregular shells.

Face normals must be coherent for the result to move consistently. Flipped normals or sharp changes can make neighboring elements travel in opposing directions, so orientation should be inspected before [[Blender Extrude Along Normals|normal-based extrusion]] or shrink/flatten operations.

# References

[[creatinggameenvironmentsinblender3d.pdf]]

