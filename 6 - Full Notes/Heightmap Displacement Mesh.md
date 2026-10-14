2026-09-28 20:13

Status: #baby

Tags: [[Blender Asset Interoperability]]

# Heightmap Displacement Mesh

A subdivided grid can become terrain when a Displace modifier uses a grayscale heightmap as its texture. Dark values lower vertices and light values raise them, while displacement strength scales the relief.

The mesh needs enough subdivisions to express the image's spatial detail. A Simple subdivision mode adds vertices without smoothing away the underlying grid form, after which the displacement remains adjustable instead of being permanently sculpted into the base mesh.

The Blender 2.77 material workflow demonstrates the same dependency at a smaller scale: enabling a texture's geometry displacement moves the mesh vertices to create lumps and depressions, and the influence value controls direction and magnitude. A low-resolution mesh cannot reproduce detail that has no vertices to move.

# References

[[howtocheatinblender27x.pdf]]

[[testdriveblender.pdf]]
