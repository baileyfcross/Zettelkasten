2026-10-03 16:11

Status: #baby

Tags: [[Numerical ODE Methods]]

# Milne Method

Milne's method is a four-step [[Predictor-Corrector Method]]. A predictor obtained by integrating a forward interpolation formula estimates the next ordinate, and a Simpson-based corrector refines it using the newly estimated slope.

Four accurate starting values are required, commonly supplied by a Taylor or Runge-Kutta procedure. Repeated correction improves the step value, but the method can be unstable because certain error components grow instead of decaying.

# References

[[numericalmethodsinengineeringandscience.pdf]]

