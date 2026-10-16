2026-10-15 10:43

Status: #baby

Tags: [[Randomized Compiling and Zero-Noise Extrapolation]]

# Infinite-Randomization Pauli-Channel Limit

The infinite-randomization limit replaces finite sampling over randomized circuit compilations with the exact Pauli-twirled channel for every noisy entangling-gate cycle. For $n$ qubits and $k$ such cycles, this has the same average effect as an ensemble of $4^{nk}$ Pauli choices, without explicitly executing every circuit in simulation.

Because the studied noise acts on nonparameterized CNOT gates, the twirled noise operators can be computed outside the VQE loop. This makes the exact ensemble average a useful simulation reference even though it is not a practical enumeration strategy on hardware.

Comparing this limit with finite ensembles separates noise-tailoring bias from randomization variance. In the infinite-randomization, infinite-shot calculation, the optimizer-dependent spread is nearly eliminated when RC and ZNE are combined, clarifying the finite-sampling behavior described in [[Optimizer Sensitivity under Finite Randomization]].

# References

[[2022 - Synergetic quantum error mitigation by randomized compiling and zero-noise extrapolation for the variational quantum eigensolver.pdf]]
