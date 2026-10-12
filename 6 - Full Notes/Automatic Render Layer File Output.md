2026-09-28 20:13

Status: #baby

Tags: [[Blender Render Optimization and Compositing]]

# Automatic Render Layer File Output

Compositor File Output nodes can save render layers automatically when rendering completes. A Render Layers input identifies each layer, and a corresponding output node defines its filename, format, and alpha-preserving color mode.

The node graph turns an error-prone manual export sequence into a repeatable pipeline. Each output should use a unique path, and compositing must be enabled so the render result actually passes through the file-writing nodes.

# References

[[howtocheatinblender27x.pdf]]
