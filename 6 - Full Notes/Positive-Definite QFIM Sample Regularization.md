2026-10-17 14:27

Status: #baby

Tags: [[Stochastic Quantum Natural-Gradient Optimization]]

# Positive-Definite QFIM Sample Regularization

Stochastic QFIM samples can be indefinite, singular, or poorly conditioned even though the exact quantum Fisher information is positive semidefinite. QN-SPSA stabilizes the accumulated estimate $A$ by replacing it with

$$
\sqrt{AA}+\beta I,
$$

where the matrix square root maps negative sampled eigenvalues to nonnegative magnitudes and $\beta>0$ makes the result invertible.

This transformation prevents an accidental negative curvature direction or a nearly zero eigenvalue from producing an unstable natural-gradient step. It is a stronger intervention than simply computing a [[Regularized Quantum Metric Pseudoinverse]] because it first repairs the sampled matrix's sign structure.

The resulting update is biased away from the exact quantum metric. That bias is deliberate: the regularizer exchanges geometric fidelity for a usable finite-sample inverse.

# References

[[2021 - Simultaneous Perturbation Stochastic Approximation of the Quantum Fisher Information.pdf]]

