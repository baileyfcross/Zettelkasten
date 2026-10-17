2026-10-16 23:00

Status: #baby

Tags: [[Quantum Invertible Generative Models]]

# Composite QINN Density-Estimation Loss

The QINN training objective combines three terms with different responsibilities:

$$L=L_{\mathrm{NLL}}+L_{\mathrm{invertibility}}+L_{\mathrm{MMD}}.$$

The negative log-likelihood fits a Gaussian latent density through the normalizing-flow change-of-variables formula. The invertibility term uses either state fidelity or round-trip reconstruction error to repair the noninvertible measurement boundary. The MMD term guides generated and latent samples toward their target distributions while that inverse is still being learned.

The terms are complementary rather than interchangeable. Likelihood supplies density estimation, [[Reconstruction MSE Invertibility Loss]] makes the classical map reversible, and [[MMD-Guided QINN Training]] stabilizes the path toward the regime where likelihood is valid.

# References

[[2023 - Generative Invertible Quantum Neural Networks.pdf]]

