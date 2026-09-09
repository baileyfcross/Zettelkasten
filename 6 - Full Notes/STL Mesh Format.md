2026-09-08 09:04

Status: #baby

Tags: [[Portable 3D Model Data]]

# STL Mesh Format

STL represents a surface as triangular facets and is common in engineering, CAD, and fabrication workflows. It can be stored in text or binary form and records a normal and three vertices for each triangle.

The format does not use shared vertex indices and does not carry texture coordinates in the representation discussed by the source. Vertices are therefore repeated wherever triangles meet. That redundancy makes STL less compact than an indexed mesh, but its simple triangular structure gives it broad interchange value for geometric surfaces.

# References

[[blenderpythonapi.pdf]]
