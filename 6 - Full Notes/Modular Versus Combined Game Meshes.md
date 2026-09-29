2026-09-28 20:13

Status: #baby

Tags: [[Blender Game Asset Export]]

# Modular Versus Combined Game Meshes

An asset should remain a separate game mesh when designers need to repeat it, place it independently, animate it separately, or use it far from related objects. Nearby static parts that always appear together may instead benefit from export as one joined mesh.

The decision is contextual rather than a universal call-count rule. Reuse and independent behavior favor modularity; fixed co-location favors consolidation. The export boundary should reflect how the engine will actually instantiate and manipulate the asset.

# References

[[howtocheatinblender27x.pdf]]
