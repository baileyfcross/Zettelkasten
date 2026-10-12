2026-09-20 23:34

Status: #baby

Tags: [[OpenGL Rendering Pipeline]]

# Mesh Rendering Component

A mesh rendering component attaches a three-dimensional mesh and material behavior to a [[Game Actor]]. During drawing it supplies the actor's world transform, binds the required shader and textures, and submits the mesh's vertex array.

Separating mesh rendering from the actor lets the same actor architecture support different visual components. The mesh asset can also be cached and shared while each component retains its own owning actor and draw state.

# References

[[gameprogrammingincplusplus.pdf]]
