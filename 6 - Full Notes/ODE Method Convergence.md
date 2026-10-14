2026-10-03 16:11

Status: #baby

Tags: [[Numerical ODE Methods]]

# ODE Method Convergence

A numerical ODE method is convergent when its approximation at a fixed point approaches the exact solution as the step size tends to zero and the error in the initial data also tends to zero.

Consistency of the local approximation is necessary, but error propagation across many steps also matters. Taylor and Runge-Kutta procedures converge under suitable smoothness, while predictor-corrector convergence can be established when the right-hand side satisfies a Lipschitz condition in the dependent variable.

# References

[[numericalmethodsinengineeringandscience.pdf]]

