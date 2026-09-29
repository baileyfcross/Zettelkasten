2026-09-28 20:13

Status: #baby

Tags: [[Blender Selection and Scene Organization]]

# Non-Manifold Boundary Selection

Non-manifold selection can expose edges that do not participate in a consistently closed surface. In an open mesh, boundary edges are connected to only one face, so selecting them reveals holes and the perimeter of missing geometry.

The selection is diagnostic rather than automatically erroneous: an intentionally open sheet also has boundary edges. Its value is that it makes topological assumptions visible before closing a model, preparing a solid, or troubleshooting export and simulation behavior.

# References

[[howtocheatinblender27x.pdf]]
