2026-10-15 00:14

Status: #baby

Tags: [[Quantum Computing for High-Energy Physics]]

# Quantum Scattering Input-State Preparation

A quantum simulation of particle scattering must prepare more than a convenient computational-basis state. Collider-like initial conditions contain localized wave packets of composite quasiparticles with controlled center-of-mass momentum and particle number. Expressed in elementary field variables, the quasiparticle's internal wavefunction can already be highly entangled.

This makes state preparation a separate problem from implementing the time-evolution operator. The simulator must begin from the dressed vacuum and manipulate encoded quantum fields into incoming composite packets without destroying gauge constraints or introducing uncontrolled excitations. A correct evolution circuit applied to the wrong incoming state does not reproduce the desired scattering experiment.

Quantum tensor-network proposals offer partial strategies, but the report identifies no general optimal construction. Work on classical tensor networks is still valuable because both tensor-network and future quantum-processor simulations use the Hamiltonian description. State preparation therefore remains a durable bottleneck across the [[Quantum Lattice Gauge Theory Dimension Roadmap]], not just a temporary limitation of small devices.

# References

[[2023 - Quantum Computing for High-Energy Physics State of the Art and Challenges Summary of the QC4HEP Working Group.pdf]]
