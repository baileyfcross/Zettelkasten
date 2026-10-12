2026-09-14 00:20

Status: #baby

Tags: [[Blender Operator and Event System]]

# Blender Event Distribution Pipeline

Blender distributes events by iterating its windows, establishing the active screen, scene, and view layer, and then consuming each [[Blender Window Event Queue]]. For every event it locates the screen area and region whose rectangles contain the relevant coordinates.

The dispatcher writes those objects into the [[Blender bContext Structure]], updates region-relative mouse coordinates, and continues through [[Blender Region Event Routing]]. [[Blender Operator Handler Dispatch]] then calls the installed handler capable of invoking the selected operation callback.

# References

[[coreblenderdevelopment.pdf]]

