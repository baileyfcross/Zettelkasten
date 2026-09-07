2026-09-06 19:44

Status: #baby

Tags: [[Nonlinear Optimization Methods]]

# Newton Root-Finding Method

Newton's root-finding method updates $x_{k+1}=x_k-f(x_k)/f'(x_k)$. It replaces the function near the current point by its tangent line and uses the tangent's intercept as the next estimate.

The method can converge rapidly near a simple root, but it requires derivatives and a suitable starting value. A zero or small derivative can make an iteration fail or jump away.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]
