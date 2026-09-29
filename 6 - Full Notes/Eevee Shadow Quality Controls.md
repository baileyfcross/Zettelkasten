2026-09-28 21:55

Status: #baby

Tags: [[Blender Render Optimization and Compositing]]

# Eevee Shadow Quality Controls

Eevee shadow quality depends on shadow-map resolution, bit depth, softness, overscan, and per-light contact-shadow settings. Increasing cube-map size and bit depth can preserve more detail, while contact shadows strengthen the small gaps where objects meet.

These controls solve different artifacts, so raising one value cannot replace the others. They also increase rendering cost, making a representative camera view the right place to judge whether the improvement is visible.

# References

[[introductiontoblender30.pdf]]
