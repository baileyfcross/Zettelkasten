2026-09-18 17:13

Status: #baby

Tags: [[Game Camera Systems]]

# Spring Follow Camera

A spring follow camera treats the desired follow position as an anchor connected to the actual camera by a damped spring. Displacement creates a restoring force, while damping reduces oscillation.

The resulting lag smooths sudden target motion and can make the view feel more natural than a rigid [[Follow Camera]]. Spring constants and damping must be tuned so responsiveness is preserved without jitter or prolonged overshoot.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
