2026-10-16 17:54

Status: #baby

Tags: [[Variational Quantum Wasserstein Anomaly Detection]]

# AnoGAN Latent Variable Optimization

AnoGAN does not treat a GAN critic's raw output as an anomaly detector, because the critic was trained to distinguish generated samples from ordinary training samples rather than ordinary samples from anomalies. Instead, it searches the latent space for a value $z_{opt}$ whose generated output $G(z_{opt})$ resembles the candidate input $x$.

The anomaly score combines a residual loss, such as $\lVert x-G(z_{opt})\rVert_1$, with a discrimination loss comparing the critic's representation of the real and reconstructed inputs. A mixing coefficient controls their relative weights. In the reported implementation the scalar critic output is used rather than an intermediate feature vector, and Adam optimizes the latent variables while the trained generator and critic remain fixed.

This search makes inference an optimization problem for every new input. Reversible generators, bidirectional GANs, or encoder-decoder designs can reduce that burden, but may require more complex quantum circuits. The later [[A-qGAN Optimization-Free Quantum Scoring]] provides a contrasting quantum-state score that avoids this per-input latent search.

# References

[[2021 - Anomaly detection with variational quantum generative adversarial networks.pdf]]
