2026-09-28 20:13

Status: #baby

Tags: [[Blender Render Optimization and Compositing]]

# Progressive Refine Rendering

Cycles' historical Progressive Refine mode updated the whole image through repeated sampling instead of completing separate tiles one at a time. The artist could set a high sample ceiling, watch the image converge, and stop when its noise level was acceptable.

This exchanges some efficiency for judgment during rendering. It is useful when the necessary sample count is unknown, but a conventional tiled render can be faster once an appropriate quality target has already been established.

# References

[[howtocheatinblender27x.pdf]]
