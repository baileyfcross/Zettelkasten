2026-10-17 14:21

Status: #baby

Tags: [[Natural-Gradient Optimization of Optical Quantum Circuits]]

# Regularized Quantum Metric Pseudoinverse

Quantum natural-gradient metrics can be singular or ill-conditioned when circuit parameters are redundant. The optical implementation stabilizes the update by adding a diagonal term before applying a [[Pseudoinverse]]:

$$\widetilde f^{+}=(f+\lambda I)^{+}.$$

The experiments use an empirically selected value near $\lambda=0.1$. The shift prevents very small metric eigenvalues from producing excessively large steps, while the pseudoinverse permits an update even when an ordinary inverse does not exist.

Regularization changes the exact natural gradient and introduces a tunable bias. Its purpose is numerical stability, so the chosen value is part of the optimizer specification rather than a property derived uniquely from the quantum geometry.

# References

[[2021 - Natural Gradient Optimization for Optical Quantum Circuits.pdf]]

