2026-10-03 16:11

Status: #baby

Tags: [[Numerical ODE Methods]]

# Step-by-Step ODE Method

A step-by-step ODE method advances the numerical solution across a grid of nearby $x$ values. Each new ordinate is computed from already available numerical data rather than from one closed-form expression for the entire interval.

Euler and Runge-Kutta methods use the most recent state, while Milne and Adams-Bashforth formulas reuse several earlier states. The latter require starting values supplied by a self-starting method such as [[Fourth-Order Runge-Kutta Method]].

# References

[[numericalmethodsinengineeringandscience.pdf]]

