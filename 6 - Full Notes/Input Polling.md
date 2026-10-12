2026-09-20 23:34

Status: #baby

Tags: [[Game Input Systems]]

# Input Polling

Input polling queries the current state of a device during the game frame. Keyboard keys, mouse buttons, controller buttons, axes, and triggers are copied into an input-state object that gameplay can inspect.

Polling gives a consistent per-frame snapshot, but edge detection requires comparison with the previous snapshot. Device events may update the same stored state while the rest of the game consumes a stable abstraction.

# References

[[gameprogrammingincplusplus.pdf]]
