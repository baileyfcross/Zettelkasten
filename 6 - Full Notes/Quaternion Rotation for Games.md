2026-09-18 17:13

Status: #baby

Tags: [[3D Game Rendering]]

# Quaternion Rotation for Games

Quaternion rotation represents a three-dimensional orientation with four values rather than an Euler-angle sequence or a full matrix. Quaternions avoid gimbal-lock behavior and support smooth interpolation between orientations.

A game object can store position, scale, and quaternion rotation compactly, then construct a temporary world matrix when rendering needs it. The multiplication still has to preserve the intended scale-rotate-translate order.

# References

[[gameprogrammingincplusplus.pdf]]
[[gameprogrammingalgorithmsandtechniques.pdf]]
