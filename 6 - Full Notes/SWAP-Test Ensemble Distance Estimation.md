2026-10-16 23:13

Status: #baby

Tags: [[Quantum State Diffusion Models]]

# SWAP-Test Ensemble Distance Estimation

QuDDPM estimates pairwise pure-state fidelities with a SWAP test. An ancilla controls swaps between corresponding qubits of two $n$-qubit states; after Hadamard operations, the probability of measuring the ancilla in $|0\rangle$ is

$$P(0)=\frac{1+|\langle\psi|\tilde\psi\rangle|^2}{2}.$$

One comparison requires $2n+1$ qubits and $n$ controlled-SWAP operations. Using a decomposition of five two-qubit gates per Fredkin gate gives an $O(5n)$ two-qubit-gate count, apart from connectivity overhead.

Ensemble losses require many such pairwise estimates. Here the overlap serves as a kernel or transport cost between samples, unlike [[SWAP-Test State-Fidelity Invertibility Loss]], which compares two states inside one model's round-trip reconstruction.

# References

[[2023 - Generative quantum machine learning via denoising diffusion probabilistic models.pdf]]

