2026-09-18 17:13

Status: #baby

Tags: [[Game Physics and Collision]]

# Velocity Verlet Integration

Velocity Verlet integration advances position using current velocity and acceleration, then updates velocity using acceleration information across the interval. It offers better stability and energy behavior than basic [[Euler Integration]] for many physical simulations.

Like other numerical integration methods, it depends on a controlled time step. It approximates continuous motion through successive discrete updates rather than producing an exact trajectory.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
