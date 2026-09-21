2026-09-20 23:34

Status: #baby

Tags: [[OpenGL Rendering Pipeline]]

# Fragment Shader

A fragment shader is a GPU program that calculates output values for a rasterized fragment, commonly its color. It receives interpolated data from the [[Vertex Shader]] and may sample textures or evaluate lighting.

Depth, blending, and other fixed-function tests determine how the result affects framebuffer attachments. In deferred shading, the shader can write several surface properties into different [[G-Buffer]] targets instead of producing final lighting immediately.

# References

[[gameprogrammingincplusplus.pdf]]
