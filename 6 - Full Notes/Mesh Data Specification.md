2026-09-08 09:04

Status: #baby

Tags: [[Portable 3D Model Data]]

# Mesh Data Specification

A polygon mesh can be specified by vertex coordinates and faces that reference those vertices. Edges may be stated explicitly or derived from face boundaries, while normals describe surface orientation for visibility and lighting. The order of indices in a face can determine which direction its normal points.

This representation separates geometry from the files and applications that carry it. Blender datablocks, OBJ, STL, and PLY make different choices about indexing and supported attributes, but each encodes enough structure to reconstruct a surface. Understanding that shared core makes import, export, and procedural creation easier to reason about.

# References

[[blenderpythonapi.pdf]]
