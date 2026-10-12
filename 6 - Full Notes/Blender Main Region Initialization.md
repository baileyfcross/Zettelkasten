2026-09-14 00:20

Status: #baby

Tags: [[Blender Editor Construction]]

# Blender Main Region Initialization

A custom editor's main-region initialization callback prepares its two-dimensional view state for the current width and height. The tutorial uses the [[Blender UI View2D API]] to reinitialize the region with a customizable common-view mode.

This setup gives the subsequent draw callback a coherent [[Blender View2D Region Coordinates]] system. The callback is registered in the main [[Blender Region Type Structure]] and runs when the editor or region requires size-dependent initialization.

# References

[[coreblenderdevelopment.pdf]]

