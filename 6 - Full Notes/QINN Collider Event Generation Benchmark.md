2026-10-16 23:00

Status: #baby

Tags: [[Quantum Invertible Generative Models]]

# QINN Collider Event Generation Benchmark

The QINN benchmark learns five observables for the simulated collider process $pp\to Zj\to\ell^+\ell^-j$: the two lepton transverse momenta, their azimuthal separation, and their two rapidities. One hundred thousand MadGraph events are split 37.5% for training, 12.5% for validation, and 50% for testing after generator-level kinematic cuts.

A five-qubit QINN uses 12 forward quantum layers, an eight-layer quantum inverse-state-preparation component, and a three-layer classical inverse-preparation network. All models train for 200 epochs, while an MMD term explicitly targets the reconstructed $Z$-boson mass.

The benchmark evaluates whether a compact simulated hybrid flow can reproduce low-level correlations and derived observables. It does not measure real-device behavior, generalization to other processes, detector effects, or end-to-end event-generation cost.

# References

[[2023 - Generative Invertible Quantum Neural Networks.pdf]]

