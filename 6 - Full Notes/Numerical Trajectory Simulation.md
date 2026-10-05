2026-10-04 22:56

Status: #baby

Tags: [[R Probability Simulation and Curve Fitting]]

# Numerical Trajectory Simulation

A numerical trajectory simulation advances position and velocity through small time steps using the force or acceleration calculated from the current state. Each step updates velocity and then position, storing the evolving coordinates for later inspection and plotting.

The student companion applies this pattern to Earth's motion under gravitational attraction. Step size controls a tradeoff between computation and integration error, so orbit shape and conserved physical quantities should be checked rather than assuming that many iterations guarantee accuracy.

# References

[[rstudentcompanion.pdf]]
