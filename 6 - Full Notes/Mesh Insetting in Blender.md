2026-09-07 23:25

Status: #baby

Tags: [[Blender Mesh Modeling and Modifiers]]

# Mesh Insetting in Blender

An inset creates a smaller face region inside selected faces and adds the surrounding connecting geometry. It may resemble extruding and scaling inward, but the dedicated operation handles complex selections more consistently.

Inset geometry prepares a surface for later extrusion, deletion, or detail work. Its boundary establishes controlled supporting edges without requiring each new edge to be placed manually.

Blender's inset controls separate thickness from depth and can switch from inset to outset. Individual processes selected faces separately, Boundary includes the outer border, Offset Even maintains more uniform width, and Edge Rail follows existing edges. Interpolation carries face data into the new region, making the operation relevant to both topology and surface attributes.

# References

[[blenderfordummies4thedition.pdf]]

[[introductiontoblender30.pdf]]

[[modelingandanimationusingblender.pdf]]
