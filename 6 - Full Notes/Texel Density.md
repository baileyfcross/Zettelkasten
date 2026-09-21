2026-09-20 23:34

Status: #baby

Tags: [[Advanced Real-Time Rendering]]

# Texel Density

Texel density is the relationship between texture samples and the screen pixels covered by a rendered surface. Magnification occurs when one texel covers many pixels; minification occurs when many texels contribute to one pixel.

Filtering quality depends on this relationship. Mipmaps aim to select a resolution near the needed density, while [[Anisotropic Filtering]] handles cases where density differs strongly along different screen directions.

# References

[[gameprogrammingincplusplus.pdf]]
