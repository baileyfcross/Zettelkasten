2026-10-01 00:39

Status: #baby

Tags: [[3D Game Rendering]]

# Scanline Rendering

Scanline rendering determines visible surfaces while producing an image one horizontal line, and ultimately one pixel, at a time. Its orderly traversal and local visibility work make it comparatively fast, which is why the method has been used where many frames must be produced efficiently.

The local nature of the scan means that effects depending on paths through the wider scene, especially naturally cast shadows and interreflection, are not inherent to the method. Those relationships require additional algorithms or a different rendering model such as [[Ray Trace Rendering]] or [[Radiosity Rendering]].

# References

[[mathematicsforcomputergraphicsandgameprogramming.pdf]]
