2026-10-12 18:17

Status: #baby

Tags: [[Policy-Gradient Variational Quantum Compilation]]

# Known-Connectivity Shallow Quantum Compilation

The paper's compilation problem assumes that the unknown target unitary has depth at most logarithmic in the number of qubits and that its qubit-connectivity graph is known. The learned variational circuit uses the same depth and connectivity, with single-qubit y rotations and two-qubit ZZ rotations in the numerical experiments.

These assumptions restrict the search to a physically motivated NISQ regime while avoiding unnecessary parameters. If connectivity were unknown, an all-to-all candidate circuit would be required, causing the number of free angles to grow quadratically with the qubit count and making the policy search less attractive.

Logarithmic depth is not a guarantee of easy training: global fidelity costs can already develop barren plateaus in this regime. The approach therefore combines the restricted circuit family with [[Gaussian Policy over Variational Circuit Angles]] rather than claiming that shallow depth alone makes compilation tractable.

# References

[[2022 - Policy Gradient Approach to Compilation of Variational Quantum Circuits.pdf]]
