2026-09-14 00:20

Status: #baby

Tags: [[Blender Editor Structure]]

# Blender Window Structure

`wmWindow` represents one Blender application window. It points back to the native window created by GHOST, selects an active [[Blender Screen Structure]], and carries input state and a [[Blender Window Event Queue]] for application-level processing.

The [[Blender Window Manager Structure]] aggregates all such windows. Each pass through event handling and the [[Blender Editor Draw Pipeline]] iterates them, sets the current window in the [[Blender bContext Structure]], and then descends through screens, areas, and regions.

# References

[[coreblenderdevelopment.pdf]]

