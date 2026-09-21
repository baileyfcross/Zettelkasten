2026-09-20 23:34

Status: #baby

Tags: [[Game Input Systems]]

# Multi-Controller Input

Multi-controller input maintains separate device handles and state snapshots for several connected controllers. Each player or local role is assigned an instance rather than assuming one global gamepad.

Connection and removal can occur at runtime, so assignments must tolerate missing or reordered devices. Per-controller button edges, axes, dead zones, and mappings are then processed through the same input abstraction.

# References

[[gameprogrammingincplusplus.pdf]]
