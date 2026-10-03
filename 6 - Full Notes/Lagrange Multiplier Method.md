2026-09-06 19:44

Status: #baby

Tags: [[Nonlinear Optimization Methods]]

# Lagrange Multiplier Method

The Lagrange multiplier method finds candidate extrema subject to equality constraints by combining the objective and constraints in a Lagrangian. Stationarity requires the objective gradient to be a linear combination of constraint gradients.

The multipliers measure the local sensitivity of the optimum to constraint bounds. Candidate points still require feasibility and classification checks.

For one smooth constraint $g(x)=c$ with $\nabla g(x)\neq0$, a constrained extremum must satisfy $\nabla f(x)=\lambda\nabla g(x)$. This condition locates candidates but does not determine whether each is a maximum or minimum.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[multivariableandvectorcalculus.pdf]]
