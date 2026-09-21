2026-09-20 23:34

Status: #baby

Tags: [[OpenGL Rendering Pipeline]]

# Texture Mapping in OpenGL

Texture mapping in OpenGL associates vertex texture coordinates with an image stored in a texture object. Rasterization interpolates the coordinates across a triangle, and the fragment shader samples the image to determine surface color or another material value.

The texture must be uploaded with a known format and bound to the sampler expected by the shader. Filtering and wrapping rules define how samples behave between texels or outside the basic coordinate range.

# References

[[gameprogrammingincplusplus.pdf]]
