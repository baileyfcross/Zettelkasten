2026-10-16 23:18

Status: #baby

Tags: [[Symmetry-Equivariant Variational Quantum Learning]]

# Nonlocality Cost of Quantum Gate Symmetrization

Group twirling can turn a local generator into a sum of symmetry-related terms spread across the register. The resulting gate is equivariant as an abstract unitary, but its interactions may be nonlocal relative to the device's coupling graph.

Compiling those interactions can require long SWAP chains or many elementary gates, increasing depth and noise exposure. A parameter reduction can therefore coexist with a larger physical circuit, so the number of trainable angles alone is not a sufficient resource measure.

This cost is separate from [[Universality Loss under Quantum Gate Symmetrization]]: one concerns whether the allowed transformation family is complete, while the other concerns whether its generators can be implemented efficiently on the target hardware.

# References

[[2022 - Exploiting symmetry in variational quantum machine learning.pdf]]

