2026-09-20 23:34

Status: #baby

Tags: [[C++ Game Engine Architecture]]

# Texture Resource Cache

A texture resource cache maps an asset name to a previously loaded texture object. When another component requests the same file, the engine returns the existing resource instead of decoding and uploading duplicate image data.

Central caching reduces memory use and loading work, but ownership must be clear. The cache should release shared textures only after dependent components are gone and the rendering context can still destroy their GPU resources.

# References

[[gameprogrammingincplusplus.pdf]]
