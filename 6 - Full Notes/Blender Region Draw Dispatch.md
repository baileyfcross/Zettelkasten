2026-09-14 00:20

Status: #baby

Tags: [[Blender Editor Construction]]

# Blender Region Draw Dispatch

Region draw dispatch connects an [[Blender Region Structure]] instance to the draw function held by its [[Blender Region Type Structure]]. After the offscreen buffer and context are prepared, the editor API obtains the runtime type and calls its registered draw callback.

Post-draw work restores pixel-space conventions and processes additional callbacks, borders, gestures, or active zones. This dispatch is the extensible endpoint of [[Blender Offscreen Editor Rendering]] and the place where a [[Blender Custom Editor Registration]] makes its own visual behavior reachable.

# References

[[coreblenderdevelopment.pdf]]

