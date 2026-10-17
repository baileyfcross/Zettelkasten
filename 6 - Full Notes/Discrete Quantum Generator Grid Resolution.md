2026-10-16 22:51

Status: #baby

Tags: [[Quantum Generative Architecture Performance]]

# Discrete Quantum Generator Grid Resolution

Allocating $r$ qubits to each of $d$ variables creates a grid with $2^r$ positions per dimension and requires $rd$ total qubits. The benchmark uses four qubits per variable, so each coordinate has only sixteen representable bins and the two- and three-dimensional circuits require eight and twelve qubits.

This coarse grid produces visibly box-shaped samples and is too low-resolution for most continuous real-world distributions. Adding more bins improves precision exponentially in $r$ but increases circuit width, gate count, simulation cost, and exposure to hardware noise.

[[Uniform Jitter for Discrete Quantum Samples]] can hide blocky plotting artifacts by spreading a selected grid point across its cell. It cannot recover within-cell structure absent from the learned discrete probabilities, so resolution remains a modeling limitation rather than only a visualization problem.

# References

[[2023 - A performance characterization of quantum generative models.pdf]]

