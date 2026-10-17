2026-10-17 14:40

Status: #baby

Tags: [[Variational Quantum Optimizer Benchmarking]]

# Hardware-Efficient Ansatz Benchmark Bias

Most circuits in the optimizer benchmark used hardware-efficient patterns built from single-qubit rotations and entangling gates. The excited-state classifier's quantum convolutional network was the principal architectural exception.

Optimizer behavior depends on the landscape induced by an ansatz. Repeated hardware-efficient layers can create parameter correlations, periodicity, and trainability problems different from symmetry-preserving, graph-structured, or chemically motivated circuits. Broad task labels do not remove this shared structural bias.

The review itself identifies quantum graph networks and symmetry-aware convolutional ansatze as missing directions. Its recommendations should thus be read as strong evidence for the tested circuit family, with architectural replication required before generalizing across all variational quantum algorithms.

# References

[[2022 - An Empirical Review of Optimization Techniques for Quantum Variational Circuits.pdf]]

