2026-10-14 17:27

Status: #baby

Tags: [[Unary-Encoded Quantum Neural Networks]]

# Fixed-Hamming-Weight Pyramid Circuit Generalization

A [[Quantum Pyramidal Circuit]] preserves total excitation number, not only unary states. If the input is restricted to $n$ qubits with Hamming weight $k$, its reachable subspace has dimension $\binom{n}{k}$, and the circuit acts there through the $k$th compound matrix of the underlying orthogonal transformation.

Unary inputs keep classical simulation to $O(n^2)$ because their subspace has dimension $n$. Higher-weight inputs enlarge the represented feature space and can combine interactions that unary encoding omits, while classical simulation grows roughly with the square of $\binom{n}{k}$. This suggests a route beyond the deliberately classical correspondence of the [[Quantum Orthogonal Neural Network]], but the paper presents it as an extension rather than a demonstrated medical-image advantage.

# References

[[2022 - Quantum Methods for Neural Networks and Application to Medical Image Classification.pdf]]
