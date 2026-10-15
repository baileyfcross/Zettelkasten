2026-10-15 00:14

Status: #baby

Tags: [[Quantum Computing for High-Energy Physics]]

# Hybrid Quantum-Classical HEP Simulation Strategy

A hybrid high-energy-physics simulation assigns different parts of a calculation to the representation that handles them best. Classical tensor networks compactly describe moderately entangled lattice states and provide strong validation baselines, while quantum circuits can represent Hilbert spaces whose full amplitudes cannot be stored directly and may continue into regimes of stronger entanglement.

The division is useful because neither side dominates every regime. Tensor networks can model equilibrium states, finite density, and some short-time or low-entanglement dynamics, but their bond dimensions grow when entanglement spreads. Quantum processors avoid explicit state-vector storage yet face shallow depth, noise, costly measurements, and difficult state preparation. A tensor-network approximation can therefore prepare or compress a state that a circuit later evolves, or serve as the reference against which a small quantum implementation is checked.

The strategy should preserve the physical interfaces between stages: gauge constraints, particle number, normalization, and observables cannot be lost when the representation changes. It complements [[Quantum Scattering Input-State Preparation]] and makes the [[Quantum Lattice Gauge Theory Dimension Roadmap]] an incremental comparison program rather than a contest based only on hardware size.

# References

[[2023 - Quantum Computing for High-Energy Physics State of the Art and Challenges Summary of the QC4HEP Working Group.pdf]]
