2026-09-07 23:25

Status: #baby

Tags: [[Blender Mesh Modeling and Modifiers]] · [[Blender Selection and Scene Organization]]

# Mesh Component Selection in Blender

A mesh is built from vertices, edges, and faces. A vertex is a point, an edge joins two vertices, and a face is a polygon bounded by at least three connected edges.

Edit mode can select any of these component types. Wireframe or X-ray display makes components on the far side selectable, while ordinary solid display limits selection to visible geometry and helps avoid unintended changes through the model.

In Blender 2.7x, more than one component-selection mode could be active at once, allowing vertices, edges, and faces to participate in the same selection. Hiding geometry also constrained later automated selections, which made visibility a practical filter for operations that would otherwise select throughout the mesh.

# References

[[blenderfordummies4thedition.pdf]]

[[howtocheatinblender27x.pdf]]
