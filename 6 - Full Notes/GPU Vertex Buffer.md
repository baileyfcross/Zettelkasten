2026-09-20 23:34

Status: #baby

Tags: [[OpenGL Rendering Pipeline]]

# GPU Vertex Buffer

A GPU vertex buffer stores vertex attribute data such as positions, texture coordinates, normals, bone indices, and weights in memory accessible to the graphics processor. A draw call interprets those bytes according to a [[Vertex Attribute Layout]].

Static geometry can be uploaded once and reused across many frames. Dynamic data requires an update strategy that avoids unnecessary transfers or synchronization with commands already using the buffer.

# References

[[gameprogrammingincplusplus.pdf]]
