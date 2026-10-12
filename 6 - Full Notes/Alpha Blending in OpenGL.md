2026-09-20 23:34

Status: #baby

Tags: [[OpenGL Rendering Pipeline]]

# Alpha Blending in OpenGL

Alpha blending in OpenGL combines a source fragment with the color already stored in the framebuffer according to configured blend factors. A common rule weights the source by its alpha and the destination by one minus source alpha.

Blending makes sprite transparency and translucent surfaces possible, but draw order matters because the operation is generally not commutative. Transparent geometry is usually rendered after opaque geometry and often requires back-to-front sorting.

# References

[[gameprogrammingincplusplus.pdf]]
