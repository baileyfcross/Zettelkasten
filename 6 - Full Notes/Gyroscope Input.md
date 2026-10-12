2026-09-18 17:13

Status: #baby

Tags: [[Game Input Systems]]

# Gyroscope Input

Gyroscope input measures the device's rotation rate around its axes. Integrated over time, it helps estimate changes in orientation, though accumulated error makes sensor fusion useful.

Device-motion APIs combine gyroscope and [[Accelerometer Input]] to expose attitude as Euler angles, a matrix, or a quaternion. This lets gameplay use orientation without reconstructing it from raw sensor readings alone.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
