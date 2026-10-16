2026-10-16 17:27

Status: #baby

Tags: [[Quantum Chebyshev Modeling]]

# Quantum Chebyshev Transform

The quantum Chebyshev transform, or QChT, is the basis-changing unitary

$$
U_{\mathrm{QChT}}=\sum_{j=0}^{2^N-1}|\tau(x_j^{\mathrm{Ch}})\rangle\langle x_j|,
$$

which maps computational-basis bitstrings to the corresponding [[Orthonormal Chebyshev Quantum State|Chebyshev basis states]]. Its columns are those of a type-II discrete cosine transform, including the different normalization of the constant Chebyshev term.

The proposed circuit realizes this relation through a quantum Fourier transform on the $N$ data qubits plus one ancilla, followed by phase corrections, a permutation network, CNOT ladders, and final amplitude and phase adjustments. The ancilla begins and ends in $|0\rangle$, so the transform acts as a clean basis conversion. Reversing the learned model and then applying QChT turns a latent Chebyshev model into a computational-basis distribution that can be sampled by measurement.

# References

[[2023 - Quantum Chebyshev Transform Mapping Embedding Learning and Sampling Distributions.pdf]]
