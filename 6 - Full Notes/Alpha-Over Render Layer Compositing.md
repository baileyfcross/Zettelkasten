2026-09-28 20:13

Status: #baby

Tags: [[Blender Render Optimization and Compositing]]

# Alpha-Over Render Layer Compositing

An Alpha Over compositor node places one RGBA render layer over another according to the upper layer's transparency. The combined result can feed both a Viewer node for inspection and a File Output node for a consolidated image.

This preserves separate layers and a finished composite in one rendering workflow. Correct ordering matters because exchanging the upper and lower inputs changes which image occludes the other.

# References

[[howtocheatinblender27x.pdf]]
