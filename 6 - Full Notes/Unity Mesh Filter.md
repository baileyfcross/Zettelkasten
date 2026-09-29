2026-09-28 22:14

Status: #baby

Tags: [[Unity Game Development]]

# Unity Mesh Filter

A Unity Mesh Filter associates a three-dimensional mesh asset with a [[Unity GameObject]]. The mesh supplies vertices and surface geometry but does not draw itself.

Visible geometry normally requires both a Mesh Filter and a [[Unity Renderer]], which combines the mesh with materials, shaders, and lighting. Keeping geometry storage separate from rendering allows the same mesh to be reused with different appearances and lets nonvisual systems refer to an object without confusing its display surface with its identity.

# References

[[introductiontogamedesignprototypinganddevelopment3e.pdf]]

