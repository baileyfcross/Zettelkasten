2026-10-14 17:27

Status: #baby

Tags: [[Unary-Encoded Quantum Neural Networks]]

# Signed Unary-State Tomography

Signed unary-state tomography estimates the real amplitudes of $|y\rangle=|Wx\rangle$, not merely their squared measurement probabilities. This distinction matters because classical activations such as ReLU behave differently on positive and negative layer outputs.

One procedure runs three related circuits: the original estimates magnitudes, and two versions with final $\pi/4$ RBS gates compare neighboring signs. Another adds an ancilla and interferes the output with a known uniform unary state, extracting each sign and magnitude from ancilla-conditioned probabilities in one deeper circuit. Both have sampling cost approximately $\widetilde O(n/\delta^2)$ for componentwise error $\delta$, creating a significant readout overhead in a [[Layerwise Hybrid Quantum Orthogonal Network]].

# References

[[2022 - Quantum Methods for Neural Networks and Application to Medical Image Classification.pdf]]
