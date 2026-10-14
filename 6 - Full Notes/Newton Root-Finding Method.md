2026-09-06 19:44

Status: #baby

Tags: [[Numerical Root-Finding Methods]]

# Newton Root-Finding Method

Newton's root-finding method updates $x_{k+1}=x_k-f(x_k)/f'(x_k)$. It replaces the function near the current point by its tangent line and uses the tangent's intercept as the next estimate.

The method can converge rapidly near a simple root, but it requires derivatives and a suitable starting value. A zero or small derivative can make an iteration fail or jump away.

Unconstrained one-dimensional optimization applies the same iteration to the derivative of an objective, giving $x_{k+1}=x_k-f'(x_k)/f''(x_k)$. This can converge quickly near a strict minimum, but a small second derivative or a start in the wrong basin can produce an unstable step or a stationary point of the wrong type.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[numericalmethodsinengineeringandscience.pdf]]

[[statisticalcomputingincplusplusandr.pdf]]
