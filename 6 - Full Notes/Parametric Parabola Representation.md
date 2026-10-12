2026-10-01 00:39

Status: #baby

Tags: [[Parametric Curve and Surface Design]]

# Parametric Parabola Representation

For a right-opening parabola y squared equals 4ax, one useful parameterization is x equals a times theta squared and y equals 2a theta. Unlike an ellipse, the parabola is open, so rendering requires finite minimum and maximum parameter values chosen from the desired x or y extent.

A constant parameter increment leads to recurrence formulas for the next x and y coordinates, making sampled generation incremental. Reflections produce other quadrants, rotation changes the axis direction, and translation moves the vertex. These transforms separate the canonical curve equation from its placement in a scene.

# References

[[mathematicsforcomputergraphicsandgameprogramming.pdf]]
