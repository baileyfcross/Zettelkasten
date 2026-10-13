2026-10-12 23:13

Status: #baby

Tags: [[Unreal Engine VR Development]]

# Parabolic VR Teleportation in Unreal Engine

Parabolic VR teleportation treats the controller direction as an initial projectile velocity and evaluates the path at fixed time steps under gravity. Unreal Engine traces each short segment from the previous sample to the next and stops at the first collision. Unlike a straight line, the arc can reach floors above or below the controller's initial direction.

The calculation separates horizontal displacement, which grows linearly with time, from vertical displacement, which subtracts one-half gravity times squared time. More samples make the collision path more faithful but perform more traces. The same sampled positions can drive a spline or beam so the player sees the proposed route and landing point before confirming it.

On activation, the pawn must be moved so the tracked camera - not merely the pawn origin - arrives at the marker. Applying the current horizontal camera-to-pawn offset prevents a room-scale user from landing beside the requested point. Teleportation reduces continuous sensory conflict compared with artificial translation, but landing feedback and orientation cues remain important because instantaneous relocation can disorient the user.

# References

[[unrealenginevrcookbook.pdf]]

