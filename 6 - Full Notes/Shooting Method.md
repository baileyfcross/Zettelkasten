2026-10-03 16:11

Status: #baby

Tags: [[Numerical ODE Methods]]

# Shooting Method

The shooting method converts a two-point boundary-value problem into a sequence of initial-value problems. An unknown initial slope is guessed, the ODE is integrated to the far boundary, and the mismatch there is used to improve the guess.

Two trial slopes allow a secant-style interpolation for the next slope. The process repeats until the computed endpoint matches the required boundary value, but convergence depends on the initial guesses and can be slow or sensitive for difficult problems.

# References

[[numericalmethodsinengineeringandscience.pdf]]

