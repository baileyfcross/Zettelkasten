2026-10-16 17:27

Status: #baby

Tags: [[Quantum Chebyshev Modeling]]

# Multivariate Quantum Chebyshev Embedding

Multivariate quantum Chebyshev embedding extends the single-variable feature map by applying separate [[Orthonormal Chebyshev Feature Map|Chebyshev maps]] to variables $x_1,\ldots,x_L$. With $N$ qubits allocated per variable, the direct tensor construction uses $LN$ data qubits and supplies products of the univariate polynomial features to a shared adjustable circuit.

The adjustable model can learn correlations across those registers, while a more structured alternative uses copula-style dependence to separate marginal distributions from their joint relationship. This extension is proposed rather than experimentally demonstrated in the paper. Its scaling and trainability therefore depend on how much of the full tensor structure is actually required, not only on the exponential polynomial degree available within each register.

# References

[[2023 - Quantum Chebyshev Transform Mapping Embedding Learning and Sampling Distributions.pdf]]
