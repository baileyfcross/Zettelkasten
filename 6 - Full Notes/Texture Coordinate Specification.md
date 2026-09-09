2026-09-08 09:04

Status: #baby

Tags: [[Portable 3D Model Data]]

# Texture Coordinate Specification

Texture coordinates associate points on a mesh surface with positions in a two-dimensional image. UV coordinates conventionally use `u` and `v` to distinguish this texture plane from the mesh's spatial `x`, `y`, and `z` axes.

A square face can map its corners to the corners of an image, while more complex surfaces require a deliberate unwrap. Coordinates outside a single unit square can repeat or tile texture data. Because texture coordinates belong to surface corners rather than merely unique spatial vertices, the same 3D point may need different UV values on adjacent faces.

# References

[[blenderpythonapi.pdf]]
