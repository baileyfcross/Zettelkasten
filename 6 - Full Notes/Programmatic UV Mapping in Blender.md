2026-09-08 09:04

Status: #baby

Tags: [[Automated Blender Texturing and Rendering]]

# Programmatic UV Mapping in Blender

Programmatic UV mapping assigns positions in a two-dimensional texture to the corners of selected mesh faces. A script first ensures a UV layer exists, retrieves it through editable mesh loop data, and writes `u` and `v` values for each relevant face corner.

Hardcoded face and loop indices can be adequate for a controlled primitive, but shared tools should identify the face by a geometric property and determine its orientation from vertex coordinates. This avoids assuming that a particular component index means the same thing after topology changes or across Blender versions.

# References

[[blenderpythonapi.pdf]]
