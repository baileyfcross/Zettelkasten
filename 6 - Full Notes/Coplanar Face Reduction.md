2026-09-08 09:04

Status: #baby

Tags: [[Portable 3D Model Data]]

# Coplanar Face Reduction

Several adjacent triangles that lie on the same plane can sometimes be represented as one polygonal face whose boundary lists all required points. This reduces the number of face records and indices without changing the visible planar surface.

The optimization depends on the target representation supporting polygon faces. OBJ and PLY can express more than three vertices in a face, whereas STL requires triangular facets. Reduction is therefore both a geometric question about coplanarity and a format question about what the receiving system accepts.

# References

[[blenderpythonapi.pdf]]
