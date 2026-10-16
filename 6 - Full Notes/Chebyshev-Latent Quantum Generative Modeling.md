2026-10-16 17:27

Status: #baby

Tags: [[Quantum Chebyshev Modeling]]

# Chebyshev-Latent Quantum Generative Modeling

Chebyshev-latent quantum generative modeling trains a probability function in the polynomial basis and samples it only after a basis change. During training, the [[Orthonormal Chebyshev Feature Map]] evaluates candidate coordinates against an adjustable circuit, producing a differentiable pointwise model $p_\theta(x)$. This latent representation makes polynomial approximation and derivative-based constraints directly accessible.

After optimization, the sampling circuit applies the inverse learned adjustable circuit to the zero state and follows it with the [[Quantum Chebyshev Transform]]. Computational-basis measurement then draws bitstrings distributed according to the learned probabilities on the [[Chebyshev Node Quantum Basis|Chebyshev grid]]. The separation unifies the two access modes in [[Explicit and Implicit Quantum Model Duality]]: pointwise evaluation for learning and projective measurement for generation.

# References

[[2023 - Quantum Chebyshev Transform Mapping Embedding Learning and Sampling Distributions.pdf]]
