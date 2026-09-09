2026-09-08 09:04

Status: #baby

Tags: [[Portable 3D Model Data]]

# Indexed Mesh Representation

An indexed mesh stores each reusable vertex once and defines faces by referring to positions in that vertex list. Normals and texture coordinates may have their own indexed collections, allowing the representation to share data where appropriate.

Compared with a naive specification that repeats every triangle's coordinates, indexing can substantially reduce file size and reveal which faces share geometric points. It also introduces ordering dependencies: a face remains meaningful only while its indices correspond to the intended entries in the referenced lists.

# References

[[blenderpythonapi.pdf]]
