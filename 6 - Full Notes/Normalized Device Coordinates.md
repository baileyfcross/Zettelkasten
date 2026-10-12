2026-09-20 23:34

Status: #baby

Tags: [[OpenGL Rendering Pipeline]]

# Normalized Device Coordinates

Normalized device coordinates are the standardized coordinates used after vertex projection and perspective division. In OpenGL, visible horizontal and vertical positions generally span from minus one to one, with depth represented in the API's normalized range.

The viewport maps this normalized cube to screen pixels. A basic 2D program can author vertices directly in this space, while a 3D program reaches it through world, view, and projection transformations.

# References

[[gameprogrammingincplusplus.pdf]]
