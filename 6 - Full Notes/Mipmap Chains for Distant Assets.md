2026-09-14 01:18

Status: #baby

Tags: [[Low-Poly Game Environment Art]]

# Mipmap Chains for Distant Assets

A mipmap chain stores progressively smaller, prefiltered versions of a texture, commonly halving each dimension at every level. A renderer selects an appropriate level as the textured object becomes smaller on screen.

This avoids repeatedly sampling a full-resolution image for a surface that covers only a few pixels. Mipmaps reduce aliasing and can improve cache use, but UV islands need adequate padding so lower-resolution filtering does not bleed unrelated colors across their boundaries.

# References

[[creatinggameenvironmentsinblender3d.pdf]]

