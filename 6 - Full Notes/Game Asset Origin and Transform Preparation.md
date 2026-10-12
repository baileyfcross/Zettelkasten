2026-09-28 20:13

Status: #baby

Tags: [[Blender Game Asset Export]]

# Game Asset Origin and Transform Preparation

Before export, a game asset needs a deliberate origin, a sensible relationship to the world origin, and normalized transform fields. Applying rotation and scale bakes the current orientation and size into the mesh while restoring rotation to zero and scale to one.

These steps reduce import offsets and coordinate surprises. The ideal origin depends on use: a center of mass suits many props, while a hinge, foot contact, or placement corner may be more useful for interactive assets.

# References

[[howtocheatinblender27x.pdf]]
