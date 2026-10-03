2026-10-03 16:11

Status: #baby

Tags: [[Numerical ODE Methods]]

# Runge Method

Runge's method samples the ODE slope at the beginning, middle, and end of a step. Simpson-style weights combine those slope estimates to approximate the solution increment.

The formula agrees with the Taylor expansion through terms of order $h^3$, so it is the third-order member of the [[Runge-Kutta Method]] family. It avoids explicit higher derivatives while requiring several evaluations of $f(x,y)$ per step.

# References

[[numericalmethodsinengineeringandscience.pdf]]

