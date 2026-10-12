2026-09-20 23:34

Status: #baby

Tags: [[Game User Interface Programming]]

# Bitmap Font Rendering

Bitmap font rendering converts text glyphs into textured images that can be drawn with the game renderer. A font library can rasterize a requested string at a chosen size, producing a texture for later interface display.

Repeated text should be cached because rasterization and texture creation are more expensive than drawing an existing result. Dynamic or frequently changing text may instead use a [[Font Texture Atlas]].

# References

[[gameprogrammingincplusplus.pdf]]
