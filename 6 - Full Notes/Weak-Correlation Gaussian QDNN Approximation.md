2026-10-12 02:19

Status: #baby

Tags: [[Quantum-Deformed Probabilistic Neural Networks]]

# Weak-Correlation Gaussian QDNN Approximation

The classical QDNN simulator approximates a binary preactivation distribution with a Gaussian whose mean and variance are computed from the deformed quantum observables. For independent activation and weight bits, this follows the usual [[Central Limit Theorem]] for a large sum of bounded random variables.

The paper extends the approximation to the correlated case by requiring correlations between sufficiently separated local terms to decay. Under that weak-correlation condition, a central-limit argument still determines the threshold probability from the preactivation's mean and variance rather than from exhaustive sampling of every binary configuration.

The approximation is efficient for the local circuit in [[Low-Entanglement Classical QDNN Simulation]], because only small-support expectation values are needed. It is not a classical simulation method for arbitrary entangling deformations; those may violate locality or decay assumptions and are precisely the cases associated with [[Quantum-Deformed Sampling Speedup]].

# References

[[2020 - Quantum Deformed Neural Networks.pdf]]
