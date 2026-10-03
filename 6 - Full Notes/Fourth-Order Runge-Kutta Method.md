2026-10-03 16:11

Status: #baby

Tags: [[Numerical ODE Methods]]

# Fourth-Order Runge-Kutta Method

The classical fourth-order Runge-Kutta method evaluates four increments $k_1,k_2,k_3,k_4$ at the beginning, two midpoint estimates, and the end of a step. It updates the solution by

$$y_{n+1}=y_n+\frac{k_1+2k_2+2k_3+k_4}{6}.$$

The weighted increment matches the Taylor solution through fourth order while using only evaluations of the ODE right-hand side. It is self-starting and widely used when a fixed-step, general-purpose method is sufficient.

# References

[[numericalmethodsinengineeringandscience.pdf]]

