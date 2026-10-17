2026-10-16 23:00

Status: #baby

Tags: [[Quantum Invertible Generative Models]]

# MMD-Guided QINN Training

Early in QINN training, the learned inverse may be poor, so the invertibility assumption behind the negative log-likelihood objective is not yet satisfied. In that regime, likelihood alone need not guide generated data or latent samples toward their target distributions.

Maximum mean discrepancy does not require an invertible map. Applying MMD on both the data and latent sides therefore supplies a distribution-level signal from the beginning of optimization. Once the reconstruction loss has established invertibility, the likelihood term becomes meaningful and can refine density estimation.

The paper interprets MMD as an optimization guide rather than the final generative objective. The round-trip reconstruction error remains below 2.1% on average in the collider benchmark, providing evidence that MMD did not simply overwhelm the learned inverse.

# References

[[2023 - Generative Invertible Quantum Neural Networks.pdf]]

