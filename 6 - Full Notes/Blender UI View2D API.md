2026-09-14 00:20

Status: #baby

Tags: [[Blender Editor Construction]]

# Blender UI View2D API

The UI View2D API provides operations for initializing and drawing within the two-dimensional view stored by an editor region. Its functions handle view reinitialization, grid and value lines, coordinate conversion, and other common behaviors needed by timeline-like or canvas-like regions.

[[Blender Main Region Initialization]] uses this interface to prepare a custom region from its current dimensions. Drawing then reads [[Blender View2D Region Coordinates]] rather than inventing a separate coordinate model, preserving compatibility with Blender's screen and region system.

# References

[[coreblenderdevelopment.pdf]]

