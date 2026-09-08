2026-09-07 23:25

Status: #baby

Tags: [[Blender Video Editing and Compositing]]

# Rendering from the Blender Compositor

Blender uses the Composite output when compositing is enabled in Output Properties. The node network must therefore lead to a meaningful Composite node if its processing is to appear in the final render.

OpenEXR MultiLayer can preserve view layers and passes for later compositing, unlike a single flattened output. This flexibility has a storage cost because each frame can contain many high-quality data channels and become very large.

# References

[[blenderfordummies4thedition.pdf]]
