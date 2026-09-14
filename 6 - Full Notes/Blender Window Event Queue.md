2026-09-14 00:20

Status: #baby

Tags: [[Blender Operator and Event System]]

# Blender Window Event Queue

Each [[Blender Window Structure]] maintains a queue of Blender event records awaiting dispatch. [[Blender GHOST Event Translation]] copies native input into the application's event representation and appends it to the active window instead of immediately guessing which editor should handle it.

Separating capture from dispatch lets [[Blender Window Event Processing]] traverse events with the current screen, scene, and view-layer context in place. Each event can then proceed through [[Blender Region Event Routing]] and its installed handler list in a controlled order.

# References

[[coreblenderdevelopment.pdf]]

