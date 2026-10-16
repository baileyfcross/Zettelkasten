2026-10-16 17:27

Status: #baby

Tags: [[Quantum Chebyshev Modeling]]

# Quantum Chebyshev Model Differentiation

A quantum Chebyshev model can be differentiated with respect to its continuous input because that input appears in the controlled phase rotations of the [[Orthonormal Chebyshev Feature Map]]. Decomposing those rotations and applying the parameter-shift rule requires two shifts for each individually reuploaded occurrence of $x$, giving $4N$ shifted evaluations for the $N$-qubit map described in the paper.

An alternative differentiates the Chebyshev-amplitude vector algebraically and represents the derivative through a [[Chebyshev Derivative Effective Generator|nonunitary effective generator]]. The first route stays close to gate-level differentiation; the second turns the derivative into weighted overlap measurements through a linear-combination construction. Input derivatives make the explicit model useful for sensitivity analysis and derivative-constrained learning, including financial Greeks and differential-equation residuals.

# References

[[2023 - Quantum Chebyshev Transform Mapping Embedding Learning and Sampling Distributions.pdf]]
