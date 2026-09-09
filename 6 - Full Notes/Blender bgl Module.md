2026-09-08 09:04

Status: #baby

Tags: [[Blender Viewport Drawing API]]

# Blender bgl Module

In the Blender 2.78c API described by the source, `bgl` wraps OpenGL-style drawing calls for the 3D Viewport and game engine. Add-ons can use it to set colors, line widths, blending state, and vertices for simple visual marks.

The source explicitly warns that this module was expected to change after Blender 2.80, so its exact calls are historical rather than timeless guidance. The durable pattern is a viewport callback that draws transient geometry, restores graphics state afterward, and leaves the scene's actual mesh data unchanged.

# References

[[blenderpythonapi.pdf]]
