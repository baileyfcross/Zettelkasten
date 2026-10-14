2026-10-01 00:39

Status: #baby

Tags: [[OpenGL Rendering Pipeline]]

# OpenGL Primitive Types

OpenGL primitive types determine how an ordered sequence of submitted vertices becomes geometry. Points use individual vertices; lines consume pairs; a line strip connects successive vertices; and a polygon interprets the sequence as one boundary.

Triangle and quadrilateral modes group vertices into independent faces, while strips reuse recent vertices to build connected faces efficiently. A triangle fan holds one common vertex while advancing around the perimeter. The primitive mode therefore supplies topology: the same vertex coordinates can produce different images depending on how OpenGL assembles them.

# References

[[mathematicsforcomputergraphicsandgameprogramming.pdf]]
