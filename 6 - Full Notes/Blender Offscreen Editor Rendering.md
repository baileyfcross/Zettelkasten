2026-09-14 00:20

Status: #baby

Tags: [[Blender Editor Construction]]

# Blender Offscreen Editor Rendering

Blender draws editor regions into offscreen buffers before copying the result to the visible window framebuffer. The window draw routine handles this offscreen pass first, then performs the onscreen composition and ultimately swaps buffers for presentation.

During the offscreen pass, Blender computes dynamic layouts, visits visible regions marked for redraw, creates and binds a region buffer, performs [[Blender Region Draw Dispatch]], and clears the redraw flag. This makes the [[Blender Editor Draw Pipeline]] update only the parts of a window that require new content.

# References

[[coreblenderdevelopment.pdf]]

