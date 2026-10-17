2026-10-17 14:21

Status: #baby

Tags: [[Natural-Gradient Optimization of Optical Quantum Circuits]]

# Singular Quantum Metric as Parameter Redundancy

A singular Fubini-Study metric means that at least one local parameter direction does not change the physical quantum state. The same state can then be represented by multiple nearby parameter values, so the state manifold has fewer effective directions than the coordinate vector.

A qubit at the north pole illustrates the effect. A rotation around the $z$ axis changes only its global phase and is therefore invisible physically, while the same rotation changes a state on the equator. The relevance of a circuit parameter can likewise depend on the current state.

Metric singularity is consequently not just a numerical failure of [[Matrix Inverse|matrix inversion]]. It records local redundancy in the chosen ansatz and motivates a [[Pseudoinverse]] or regularization rather than pretending that every coordinate direction is independent.

# References

[[2021 - Natural Gradient Optimization for Optical Quantum Circuits.pdf]]

