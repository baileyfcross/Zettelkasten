2026-10-17 14:27

Status: #baby

Tags: [[Stochastic Quantum Natural-Gradient Optimization]]

# Variational Quantum Imaginary-Time Evolution

Imaginary-time evolution suppresses excited-state amplitudes under $e^{-\tau H}$ and approaches a ground state when the initial state has nonzero ground-state overlap. A variational implementation uses McLachlan's principle to project that nonunitary trajectory onto a parameterized quantum circuit.

The parameter velocity satisfies

$$
\sum_j g_{ij}\frac{d\theta_j}{d\tau}
=-\operatorname{Re}\langle\partial_i\psi|H|\psi\rangle,
$$

where $g$ is the Fubini-Study metric. For an energy objective, this is a quantum natural-gradient flow up to a constant convention.

QN-SPSA can replace the exact metric with sampled overlaps. Because imaginary-time evolution aims to follow an entire physical trajectory rather than merely find any descending optimization path, it may require several metric samples per time step to control accumulated integration error.

# References

[[2021 - Simultaneous Perturbation Stochastic Approximation of the Quantum Fisher Information.pdf]]

