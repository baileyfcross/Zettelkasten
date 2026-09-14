2026-09-07 23:25

Status: #baby

Tags: [[Blender Materials and Textures]] · [[Blender UV Mapping and UDIM]]

# UV Unwrapping and Seams in Blender

UV unwrapping maps a three-dimensional mesh onto a two-dimensional coordinate layout, like relating a globe to a flat map. Blender's UV Editing workspace places the mesh and its UV coordinates side by side.

Seams tell Blender where the surface may be cut open for flattening. A thoughtful seam layout reduces stretching and produces islands that are easier to paint; pinned control vertices and Live Unwrap can refine the arrangement interactively.

A production-ready layout also avoids unintended overlaps, preserves padding for mipmaps, uses the square texture area efficiently, and keeps island scale proportional to required detail. Hidden or naturally occurring object seams often provide the least visible cut locations.

# References

[[blenderfordummies4thedition.pdf]]

[[creatinggameenvironmentsinblender3d.pdf]]
