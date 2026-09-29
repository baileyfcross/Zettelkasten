2026-09-28 20:13

Status: #baby

Tags: [[Blender Render Optimization and Compositing]]

# Blender Render Layer Separation

In Blender 2.7x, render layers associated selected scene layers with distinct rendered outputs. Foreground and background objects could therefore be rendered separately while still belonging to one scene and one render operation.

Separating elements increases compositing control because effects, blending, and correction can target one layer without rerendering every other element. Transparent film output and RGBA color preserve empty areas so the layers can later be stacked cleanly.

# References

[[howtocheatinblender27x.pdf]]
