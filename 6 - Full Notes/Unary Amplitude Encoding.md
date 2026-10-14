2026-10-14 17:27

Status: #baby

Tags: [[Unary-Encoded Quantum Neural Networks]]

# Unary Amplitude Encoding

Unary amplitude encoding maps a normalized real vector $x\in\mathbb{R}^d$ to the single-excitation state

$$
|x\rangle=\sum_{i=1}^{d}x_i|e_i\rangle,
$$

where $|e_i\rangle$ has exactly one qubit in state $|1\rangle$. It therefore uses $d$ qubits for $d$ features, unlike logarithmic-width [[Amplitude Encoding for Circuit-Centric Classification]], but confines computation to a transparent $d$-dimensional subspace.

The map preserves Euclidean distance between normalized vectors: $\||x\rangle-|x'\rangle\|_2=\|x-x'\|_2$. Number-preserving gates keep the state inside this subspace, which supports [[Unary-Subspace Orthogonal Matrix Multiplication]] and makes many invalid hardware outcomes detectable by [[Unary-State Postselection Error Mitigation]].

# References

[[2022 - Quantum Methods for Neural Networks and Application to Medical Image Classification.pdf]]
