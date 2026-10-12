2026-10-03 16:11

Status: #baby

Tags: [[Numerical ODE Methods]]

# Modified Euler Method

The modified Euler method predicts a value with [[Euler Method]] and corrects it using the average of the slopes at the beginning and predicted end of the step.

The endpoint value can be substituted repeatedly into the corrector until successive results agree. This mean-slope construction is a second-order Runge-Kutta method and is generally more accurate than ordinary Euler stepping at the same step size.

# References

[[numericalmethodsinengineeringandscience.pdf]]

