2026-09-08 09:04

Status: #baby

Tags: [[Portable 3D Model Data]]

# PLY Polygon Format

PLY is a polygon file format associated with captured and scanned 3D data. A header declares the elements and properties that follow, after which vertex records and face records describe the model.

Faces index the vertex list and can contain a varying number of points rather than requiring every surface to be triangulated. In the minimal form examined by the source, PLY does not carry normals or texture coordinates. Its explicit header and simple data sections make the file's schema visible to programs that read it.

# References

[[blenderpythonapi.pdf]]
