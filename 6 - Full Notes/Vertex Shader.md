2026-09-20 23:34

Status: #baby

Tags: [[OpenGL Rendering Pipeline]]

# Vertex Shader

A vertex shader is a GPU program executed for each submitted vertex. It reads attributes and uniform data, performs transformations or deformation, and must output the vertex position in clip space.

Additional outputs such as texture coordinates, normals, or world positions are interpolated across the primitive for the [[Fragment Shader]]. The shader's declared inputs must match the mesh's [[Vertex Attribute Layout]].

# References

[[gameprogrammingincplusplus.pdf]]
