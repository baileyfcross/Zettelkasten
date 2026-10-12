2026-09-28 21:55

Status: #baby

Tags: [[Blender Lighting and Rendering]]

# Blender Sky Texture Algorithms

The Sky Texture node procedurally generates physically motivated sky color and illumination. Blender 3.0 offers Nishita, Hosek-Wilkie, and Preetham models, whose turbidity, sun direction, and other atmospheric controls produce different outdoor-lighting responses.

Because the sky is procedural, it can be adjusted without loading an image map. Engine support is version-specific: the source notes that Nishita was not available in Eevee at that time, so the chosen renderer constrains the usable model.

# References

[[introductiontoblender30.pdf]]
