2026-09-14 00:20

Status: #baby

Tags: [[Blender Editor Structure]]

# Blender ED API

The ED API is the public interface supplied by the [[Blender Editors Module]]. Its declarations live in the editor include directory, while the space API source implements functions for registering space types, iterating screen areas, drawing regions, and coordinating common editor behavior.

Higher modules and individual editors use this boundary rather than reaching through each other's implementation files. [[Blender Editor Registration]], [[Blender Region Draw Dispatch]], and [[Blender Event Distribution Pipeline]] all rely on ED functions to move between window-manager logic and editor-specific callbacks.

# References

[[coreblenderdevelopment.pdf]]

