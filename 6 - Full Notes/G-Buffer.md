2026-09-20 23:34

Status: #baby

Tags: [[Advanced Real-Time Rendering]]

# G-Buffer

A G-buffer is the collection of screen-sized render targets produced by the geometry pass of [[Deferred Shading]]. Its attachments store data such as diffuse color, surface normal, world position, and depth for the nearest visible surface.

The lighting pass reconstructs its calculation from these per-pixel properties without drawing the original meshes again. Attachment formats must balance precision and bandwidth because every visible pixel writes and later reads several values.

# References

[[gameprogrammingincplusplus.pdf]]
