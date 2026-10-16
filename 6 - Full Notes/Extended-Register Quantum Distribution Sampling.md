2026-10-16 17:27

Status: #baby

Tags: [[Quantum Chebyshev Modeling]]

# Extended-Register Quantum Distribution Sampling

Extended-register quantum distribution sampling evaluates a learned Chebyshev model on a finer set of output nodes than the register used during variational training. Because the learned object is a polynomial function rather than an unrelated probability assigned to every bitstring, its optimized parameters can be reused while a larger [[Quantum Chebyshev Transform]] maps the model onto more computational outcomes.

In the paper's linear-distribution demonstration, a two-qubit Chebyshev model is mapped to an eight-qubit sampling register, producing samples across 256 Chebyshev-node labels. The extension increases output resolution; it does not retroactively add independent training information or guarantee accuracy between poorly constrained points. Its reliability depends on the polynomial basis and the quality of the learned latent function described by [[Chebyshev-Latent Quantum Generative Modeling]].

# References

[[2023 - Quantum Chebyshev Transform Mapping Embedding Learning and Sampling Distributions.pdf]]
