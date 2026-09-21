2026-09-20 23:34

Status: #baby

Tags: [[OpenGL Rendering Pipeline]]

# GPU Index Buffer

A GPU index buffer stores integer references into a [[GPU Vertex Buffer]]. Triangles can reuse shared vertices instead of repeating the same attribute data for every corner.

The index type and count supplied to the draw command must match the stored representation. Reuse reduces memory and vertex-shader work, especially in connected meshes whose neighboring triangles share positions and other attributes.

# References

[[gameprogrammingincplusplus.pdf]]
