2026-09-20 23:34

Status: #baby

Tags: [[OpenGL Rendering Pipeline]]

# Vertex Array Object

A vertex array object records the OpenGL bindings and attribute declarations needed to interpret a mesh's vertex and index buffers. Binding it restores the association between buffers and shader input locations for a draw.

The object does not replace the buffer data; it captures the configuration that explains that data. This reduces repeated state setup and keeps each mesh's [[Vertex Attribute Layout]] together.

# References

[[gameprogrammingincplusplus.pdf]]
