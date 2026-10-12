2026-09-20 23:34

Status: #baby

Tags: [[Advanced Real-Time Rendering]]

# Nearest-Neighbor Texture Filtering

Nearest-neighbor texture filtering chooses the texel center closest to a requested texture coordinate and returns that texel's value. It is inexpensive and preserves hard pixel boundaries.

When a texture is magnified, the method produces visible blocks; when minified, it can flicker or alias because many source texels compete for one pixel. The look can be intentional for pixel art but unsuitable for smoothly detailed surfaces.

# References

[[gameprogrammingincplusplus.pdf]]
