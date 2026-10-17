2026-10-17 14:27

Status: #baby

Tags: [[Stochastic Quantum Natural-Gradient Optimization]]

# Quantum-State Overlap Estimation Tradeoff

QN-SPSA replaces many analytic QFIM elements with four state-overlap evaluations, but an overlap is not a cost-free primitive. A SWAP test can compare two prepared states with roughly twice the state-register width and only modest extra depth.

A compute-uncompute circuit instead prepares

$$
U^\dagger(\theta+\delta)U(\theta)|0\rangle
$$

and measures the probability of returning to the all-zero state. It keeps the original register width but roughly doubles state-preparation depth. Randomized-measurement alternatives avoid doubling both resources but can require exponentially many measurements.

The useful resource comparison is therefore not only four overlaps versus a quadratic number of metric elements. It must include circuit width, depth, and shot complexity on the target hardware.

# References

[[2021 - Simultaneous Perturbation Stochastic Approximation of the Quantum Fisher Information.pdf]]

