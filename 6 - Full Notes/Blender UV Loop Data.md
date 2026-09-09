2026-09-08 09:04

Status: #baby

Tags: [[Automated Blender Texturing and Rendering]]

# Blender UV Loop Data

Blender stores UV coordinates on loop data associated with face corners rather than only on unique mesh vertices. For a given face and corner, the loop's UV value corresponds to that face's vertex coordinate, creating a path between topology and texture placement.

Several face corners can occupy the same point in 3D space while holding different UV coordinates. This is necessary at texture seams, where one geometric vertex appears in separate parts of the flattened image. Algorithms must therefore identify the face corner, not just the spatial vertex, when assigning UVs.

# References

[[blenderpythonapi.pdf]]
