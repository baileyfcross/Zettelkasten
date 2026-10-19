2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Graphics and 3D]]

# JavaFX Phong Materials and Texture Maps

`PhongMaterial` is the practical JavaFX material for describing how a 3D surface responds to light. It can use diffuse and specular colors as well as image maps for diffuse color, specular response, bump information, and self-illumination. A self-illumination map remains visible without external light, while a bump map encodes surface-normal variation rather than color.

Texture coordinates associate points in an image with the triangular faces of a mesh. Each face references both geometric vertices and texture positions, letting an image wrap across a custom `TriangleMesh`; built-in shapes are also mesh-based internally and can be textured. Material interpretation depends on [[JavaFX 3D Lighting]], while the underlying face structure comes from [[JavaFX 3D Shapes and Meshes]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
