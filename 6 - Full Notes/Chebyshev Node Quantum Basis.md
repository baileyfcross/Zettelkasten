2026-10-16 17:27

Status: #baby

Tags: [[Quantum Chebyshev Modeling]]

# Chebyshev Node Quantum Basis

The Chebyshev node quantum basis associates the $2^N$ computational labels $j$ with the nonuniform grid

$$
x_j^{\mathrm{Ch}}=\cos\left(\frac{\pi(2j+1)}{2^{N+1}}\right).
$$

The weighted polynomial vectors evaluated at these roots satisfy a discrete orthogonality relation, so their quantum states obey $\langle\tau(x_j^{\mathrm{Ch}})|\tau(x_{j'}^{\mathrm{Ch}})\rangle=\delta_{j,j'}$. Unlike a uniformly spaced computational grid or the evenly spaced phases of a Fourier basis, these nodes cluster toward the interval endpoints.

Measurements after a [[Quantum Chebyshev Transform]] therefore return integer bitstrings whose physical coordinates must be interpreted through this cosine map. Between the nodes, overlaps are nonzero and follow the Chebyshev reproducing-kernel structure, so the orthonormal claim applies to the selected grid rather than to every continuous $x$.

# References

[[2023 - Quantum Chebyshev Transform Mapping Embedding Learning and Sampling Distributions.pdf]]
