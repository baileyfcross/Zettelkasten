2026-10-16 17:27

Status: #baby

Tags: [[Quantum Chebyshev Modeling]]

# Chebyshev versus Fourier Quantum Distribution Models

Chebyshev and Fourier quantum models can have similar nominal expressivity while imposing different inductive biases. Fourier features naturally represent periodic or harmonic structure, whereas Chebyshev polynomials are well matched to polynomial approximation on a bounded interval and avoid forcing periodic continuation at the endpoints.

In the paper's two-qubit experiment on the linear density $P(x)=x$, the orthonormal Chebyshev model follows the target closely and its derivative stays near one. The Fourier model oscillates around the line and its derivative departs substantially from the target, which would amplify errors in a derivative-based loss. This comparison is a task-specific simulation rather than a universal superiority claim: it shows that basis selection can dominate model quality when the target's structure aligns with one basis.

# References

[[2023 - Quantum Chebyshev Transform Mapping Embedding Learning and Sampling Distributions.pdf]]
