2026-10-16 17:27

Status: #baby

Tags: [[Quantum Chebyshev Modeling]]

# Linear Combination of Unitaries for Chebyshev Models

Linear combination of unitaries, or LCU, represents a desired nonunitary operation through a weighted superposition of unitary branches in an enlarged circuit. Ancillas select and interfere the branches, while postselection or an equivalent amplitude-management step isolates the required combination.

The Chebyshev framework uses this idea in two places. The [[Orthonormal Chebyshev Feature Map]] combines positive- and negative-phase exponentials so their sum produces cosine amplitudes $T_k(x)=\cos(k\arccos x)$. [[Chebyshev Derivative Effective Generator]] uses the same general strategy to embed the nonunitary operator that maps a Chebyshev-amplitude state to its derivative. In both cases, LCU is the implementation mechanism, so its ancilla and success behavior remain part of the resource cost.

# References

[[2023 - Quantum Chebyshev Transform Mapping Embedding Learning and Sampling Distributions.pdf]]
