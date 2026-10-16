2026-10-16 17:27

Status: #baby

Tags: [[Quantum Chebyshev Modeling]]

# Chebyshev Derivative Effective Generator

The derivative of a first-kind Chebyshev polynomial can be expanded in lower-degree Chebyshev polynomials: $T_n'(x)=nU_{n-1}(x)$, with the second-kind polynomial further expressible as a parity-matched sum of $T_k(x)$. Consequently, the derivative state can be written formally as

$$
|\tau'(x)\rangle=G_{\mathrm{eff}}|\tau(x)\rangle.
$$

The effective generator $G_{\mathrm{eff}}$ is not unitary, so it cannot simply be inserted as an ordinary quantum gate. [[Linear Combination of Unitaries for Chebyshev Models]] can embed it in a larger Hilbert space, after which the derivative of a probability model is assembled from weighted overlaps involving the original and derivative states. Normalization factors for $|\widetilde\tau(x)\rangle$ must remain in the calculation because the unnormalized polynomial vector changes length away from the nodes.

# References

[[2023 - Quantum Chebyshev Transform Mapping Embedding Learning and Sampling Distributions.pdf]]
