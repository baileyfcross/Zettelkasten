2026-10-17 14:27

Status: #baby

Tags: [[Stochastic Quantum Natural-Gradient Optimization]]

# QN-SPSA Adaptive Sampling Strategies

QN-SPSA need not use the same number of metric samples at every iteration. Early iterations can use ordinary SPSA while accumulating curvature information, or average many initial QFIM samples before switching to a cheaper steady-state update.

The perturbation size can also be calibrated against hardware noise, and the number of samples can increase when a proposed step is rejected by a blocking rule. Such a rule compares the candidate loss with the current loss plus a tolerance; under measurement noise, a tolerance around twice the loss standard deviation avoids rejecting ordinary fluctuations.

These strategies allocate measurements where uncertainty is most consequential rather than enforcing a fixed schedule. They are proposals and implementation heuristics in the paper, not a demonstrated optimal controller.

# References

[[2021 - Simultaneous Perturbation Stochastic Approximation of the Quantum Fisher Information.pdf]]

