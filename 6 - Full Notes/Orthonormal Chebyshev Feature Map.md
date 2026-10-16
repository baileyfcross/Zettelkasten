2026-10-16 17:27

Status: #baby

Tags: [[Quantum Chebyshev Modeling]]

# Orthonormal Chebyshev Feature Map

The orthonormal Chebyshev feature map is a continuously parameterized quantum isometry that prepares $|\widetilde\tau(x)\rangle$, whose amplitudes are normalized Chebyshev polynomials of $x$. It first uses phase maps for scaled versions of $\arccos(x)$ to create complex exponentials and then interferes the positive- and negative-phase branches so that their sum produces cosine amplitudes.

A [[Linear Combination of Unitaries for Chebyshev Models|linear combination of unitaries]] supplies that interference, a fixed Grover-style rotation corrects the special normalization of $T_0(x)$, and an ancilla is postselected in $|0\rangle$. Earlier Chebyshev feature maps could expose polynomial features without forming an orthonormal basis; orthonormality at the designated nodes is the extra property that permits conversion to amplitude encoding and later sampling through the [[Quantum Chebyshev Transform]].

# References

[[2023 - Quantum Chebyshev Transform Mapping Embedding Learning and Sampling Distributions.pdf]]
