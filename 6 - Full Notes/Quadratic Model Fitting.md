2026-10-04 22:56

Status: #baby

Tags: [[R Probability Simulation and Curve Fitting]]

# Quadratic Model Fitting

Quadratic model fitting estimates coefficients in $y=b_1+b_2x+b_3x^2$ by minimizing the sum of squared prediction errors. The graph is curved, but the model is linear in its coefficients, so a design matrix with constant, $x$, and $x^2$ columns supports ordinary linear least squares.

The fitted curve should be plotted with the observations and interpreted only over a scientifically plausible input range. A low residual sum of squares does not make unbounded extrapolation of the parabola realistic.

# References

[[rstudentcompanion.pdf]]
