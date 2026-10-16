2026-10-16 17:27

Status: #baby

Tags: [[Quantum Chebyshev Modeling]]

# Lognormal Distribution Learning with Quantum Chebyshev Models

Geometric Brownian motion makes an asset price lognormally distributed under the Black-Scholes assumptions of constant drift and volatility. The paper uses this financially motivated density as a test of [[Chebyshev-Latent Quantum Generative Modeling]], training the probability function at positive Chebyshev nodes and additional midpoint samples.

Its simulation uses a five-qubit [[Orthonormal Chebyshev Feature Map]], a depth-14 hardware-efficient adjustable circuit, mean-squared-error training for 5,000 epochs, and a learning rate of $0.005$. After training, the inverse model and [[Quantum Chebyshev Transform]] generate a one-million-shot histogram that follows the target lognormal shape. The example demonstrates a working learning-to-sampling pipeline; it does not by itself establish a runtime advantage over classical lognormal sampling.

# References

[[2023 - Quantum Chebyshev Transform Mapping Embedding Learning and Sampling Distributions.pdf]]
