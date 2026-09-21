2026-09-20 23:34

Status: #baby

Tags: [[Advanced Real-Time Rendering]]

# Bilinear Texture Filtering

Bilinear texture filtering samples the four texels surrounding a texture coordinate and blends them according to horizontal and vertical distance. The weighted average smooths magnified textures compared with [[Nearest-Neighbor Texture Filtering]].

It operates within one mip level and can blur a texture when many texels shrink into one pixel. Mipmapping addresses that minification case by supplying lower-resolution source images.

# References

[[gameprogrammingincplusplus.pdf]]
