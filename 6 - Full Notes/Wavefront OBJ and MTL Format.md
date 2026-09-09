2026-09-08 09:04

Status: #baby

Tags: [[Portable 3D Model Data]]

# Wavefront OBJ and MTL Format

Wavefront OBJ is a human-readable interchange format for mesh geometry. It can declare vertices, texture coordinates, normals, and faces that index those collections. Its companion MTL file describes material-related information referenced by the model.

OBJ's indexed faces can reuse a vertex across several polygons and can represent faces with more than three coplanar points. This makes the format relatively compact and understandable, while its deliberately limited scope also makes it more portable than an application-native project file.

# References

[[blenderpythonapi.pdf]]
