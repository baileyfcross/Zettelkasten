2026-10-17 14:27

Status: #baby

Tags: [[Stochastic Quantum Natural-Gradient Optimization]]

# Quantum Natural SPSA

Quantum natural SPSA, or QN-SPSA, replaces the explicitly measured quantum Fisher information matrix in a natural-gradient update with a stochastic second-order estimate. It applies the [[Second-Order Simultaneous Perturbation Approximation]] to the fidelity between nearby parameterized quantum states rather than to the optimization loss itself.

Each metric sample requires four state-overlap evaluations regardless of parameter count. The sampled metric is smoothed and regularized, then combined with an SPSA loss-gradient estimate to produce a geometry-aware step.

QN-SPSA trades exact local geometry for constant quantum-query complexity. It can approach the path of an exact quantum natural gradient as metric samples accumulate, while retaining the sampling variance, inverse bias, overlap-circuit overhead, and hyperparameter sensitivity of a stochastic second-order method.

# References

[[2021 - Simultaneous Perturbation Stochastic Approximation of the Quantum Fisher Information.pdf]]

