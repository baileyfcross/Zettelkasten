2026-10-01 00:39

Status: #baby

Tags: [[OpenGL Rendering Pipeline]]

# Immediate-Mode Vertex Specification

In immediate-mode OpenGL, a drawing command begins a primitive, submits its vertices one by one, and ends the primitive. The suffix of a vertex function communicates the number and type of coordinate arguments, such as two integer components or three floating-point components.

The primitive chosen at the beginning determines how the submitted sequence is grouped into points, lines, strips, triangles, or polygons. Attributes held in OpenGL state apply as vertices pass through the command stream. A flush command can ensure that buffered drawing requests are sent for execution and display.

# References

[[mathematicsforcomputergraphicsandgameprogramming.pdf]]
