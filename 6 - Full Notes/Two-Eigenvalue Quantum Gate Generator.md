2026-10-17 14:34

Status: #baby

Tags: [[Quantum Circuit Gradient Rules]]

# Two-Eigenvalue Quantum Gate Generator

An $r$-gate is a parameterized unitary $e^{-i\theta G}$ whose [[Hermitian Matrix|Hermitian generator]] $G$ has exactly two eigenvalues separated by $2r$. A global phase can recenter those eigenvalues at $+r$ and $-r$ without changing any expectation value.

Under that convention, $G^2=r^2I$ and the gate has the expansion

$$
e^{-i\theta G}=\cos(r\theta)I-i\frac{G}{r}\sin(r\theta).
$$

This two-frequency structure is what permits exact shifted-circuit derivative identities. Gates with more than two distinct generator eigenvalues fall outside the paper's $r$-gate family and require decomposition or a more general gradient construction.

# References

[[2021 - Single-component gradient rules for variational quantum algorithms.pdf]]

