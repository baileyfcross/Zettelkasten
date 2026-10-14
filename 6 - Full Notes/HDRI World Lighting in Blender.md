2026-09-28 21:55

Status: #baby

Tags: [[Blender Lighting and Rendering]]

# HDRI World Lighting in Blender

An HDRI environment map supplies a wide luminance range to the World shader, allowing its pixels to illuminate the scene and appear in glossy reflections. Connecting an Environment Texture to the Background node makes the image a source of both surroundings and indirect light.

Mapping nodes rotate or position the environment, and Background strength controls its contribution. OpenEXR and Radiance HDR preserve high-dynamic-range data better than ordinary display images, which is why they are suited to environment illumination.

# References

[[introductiontoblender30.pdf]]
