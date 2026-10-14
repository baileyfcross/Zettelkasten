2026-09-28 20:13

Status: #baby

Tags: [[Blender Game Asset Export]]

# Simplified Collision Meshes

A collision mesh is an invisible low-complexity approximation used for physical contact instead of the rendered asset's detailed surface. Basic primitives are cheapest, while a heavily decimated duplicate can represent a more complicated volume when boxes or capsules are insufficient.

Because players never see the proxy, its geometry can be much coarser than the display mesh. It must still preserve gameplay-relevant boundaries; excessive simplification can create floating contacts, blocked openings, or passage through visible solids.

# References

[[howtocheatinblender27x.pdf]]
