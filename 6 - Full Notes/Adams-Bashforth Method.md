2026-10-03 16:11

Status: #baby

Tags: [[Numerical ODE Methods]]

# Adams-Bashforth Method

The Adams-Bashforth method predicts the next ODE value by integrating an interpolation polynomial through several previously computed derivative values. The four-step version combines the four latest slopes with fixed unequal weights.

An Adams-Moulton-style implicit formula can then correct the prediction using the slope at the new point. The method reuses old evaluations efficiently over a long interval but needs accurate starting values from a self-starting algorithm.

# References

[[numericalmethodsinengineeringandscience.pdf]]

