2026-09-20 23:34

Status: #baby

Tags: [[Advanced Real-Time Rendering]]

# Render to Texture

Render to texture directs graphics output into a texture attachment instead of the window's back buffer. The resulting image can be sampled in a later pass like any other texture.

Mirrors, cameras, post-processing, shadow maps, and deferred shading all use this pattern. The engine binds a [[Framebuffer Object]], renders with an appropriate viewpoint or shader, then restores the main framebuffer before displaying the texture.

# References

[[gameprogrammingincplusplus.pdf]]
