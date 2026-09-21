2026-09-18 17:13

Status: #baby

Tags: [[Game Physics and Collision]]

# Euler Integration

Euler integration advances a simulated quantity by adding its current rate multiplied by the time step. In linear motion, acceleration updates velocity and velocity updates position.

The method is simple but accumulates numerical error and can become unstable when the time step varies or grows too large. Physics simulation therefore commonly uses a consistent fixed step even when rendering frames arrive at irregular intervals.

# References

[[gameprogrammingincplusplus.pdf]]
[[gameprogrammingalgorithmsandtechniques.pdf]]
