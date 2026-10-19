2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Graphics and 3D]]

# JavaFX 3D Shapes and Meshes

JavaFX provides `Sphere`, `Box`, and `Cylinder` as built-in `Shape3D` nodes. Shape3D state includes material, draw mode, and face-culling behavior, so these primitives can be inserted into the same scene graph as two-dimensional nodes. Division parameters control the geometric detail used to approximate curved surfaces.

Custom objects use `MeshView` with a `Mesh`, commonly a `TriangleMesh`. The mesh stores points, texture coordinates, faces, and optionally normals; face indices connect vertex and texture data into triangles. This makes geometry independent from its [[JavaFX Phong Materials and Texture Maps|material]] and projection. JavaFX selects a hardware-accelerated rendering pipeline when available and reports missing 3D support instead of silently delivering an unusably slow scene.

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
