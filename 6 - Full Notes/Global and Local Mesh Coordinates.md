2026-09-08 09:04

Status: #baby

Tags: [[Procedural Mesh Editing with bmesh]]

# Global and Local Mesh Coordinates

Local mesh coordinates describe a component relative to its object's origin and transform, while global coordinates describe the component's position in the scene. Multiplying a local vertex coordinate by the object's world matrix produces its global position.

The distinction determines whether a geometric test follows the mesh's internal shape or its visible placement. Applying an object's transforms updates local mesh data to incorporate the world placement without visibly moving the object. A location-based algorithm must therefore declare which coordinate system its bounds and comparisons use.

# References

[[blenderpythonapi.pdf]]
