2026-10-12 17:40

Status: #baby

Tags: [[Variable-Structure Variational Quantum Circuits]]

# VAns Quantum Fourier Transform Compilation

VAns compiles a ten-qubit quantum Fourier transform by training a circuit on 15 orthogonal input-output state pairs. The training loss compares the learned and exact outputs only on those sampled states, while a separate full-unitary distance checks whether this smaller training objective tracks the complete transformation.

In the reported simulation, the full-unitary distance falls below 10^-9 and the final VAns circuit uses 48 general two-qubit gates. The hardware-efficient comparison uses 219 such gates, more than four times as many, and requires a recursively grown construction from smaller transforms; VAns is initialized randomly at ten qubits and does not use that recursive structure.

The authors rely on a prior generalization result to justify using a training set much smaller than the full 2^n state basis. The benchmark is still a numerical compilation result with unconstrained all-to-all connectivity and general two-qubit gates, so physical compilation into a particular device's native gates could change the realized depth.

# References

[[2022 - A semi-agnostic ansatz with variable structure for quantum machine learning.pdf]]
