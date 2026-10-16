2026-10-16 17:27

Status: #baby

Tags: [[Quantum Chebyshev Modeling]]

# Orthonormal Chebyshev Quantum State

An orthonormal Chebyshev quantum state stores first-kind [[Chebyshev Polynomial|Chebyshev polynomials]] as amplitudes. For $N$ qubits, the unnormalized construction assigns a separately scaled constant term to $|0\rangle$ and assigns $T_k(x)$ to basis state $|k\rangle$ for $1\leq k<2^N$.

At the [[Chebyshev Node Quantum Basis|Chebyshev nodes]], the resulting $2^N$ states are mutually orthonormal. For an arbitrary $x\in(-1,1)$, the same polynomial-amplitude vector is generally neither orthogonal to neighboring states nor automatically normalized, so the feature-map circuit prepares its normalized version $|\widetilde\tau(x)\rangle$. This node-dependent distinction is what makes a reversible [[Quantum Chebyshev Transform]] possible without claiming that every continuously parameterized state is orthogonal.

# References

[[2023 - Quantum Chebyshev Transform Mapping Embedding Learning and Sampling Distributions.pdf]]
