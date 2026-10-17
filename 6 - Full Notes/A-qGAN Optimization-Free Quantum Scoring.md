2026-10-15 10:16

Status: #baby

Tags: [[A-qGAN Anomaly Detection in High-Energy Physics]]

# A-qGAN Optimization-Free Quantum Scoring

Classical GAN anomaly detection often evaluates a new event through [[AnoGAN Latent Variable Optimization]], searching for a noise vector $z_{opt}$ whose generated sample resembles that event. The anomaly score therefore contains a new optimization problem for every point being tested, combining reconstruction distance with the discriminator's response.

The A-qGAN score removes this per-event latent search. Its generator prepares one quantum state representing the learned distribution, and each embedded test state is compared directly with that state and with the discriminator outputs. The stochasticity required to represent a distribution comes from quantum measurement rather than from supplying and optimizing a classical random input for each event.

Eliminating latent optimization simplifies inference, but it replaces that cost with state preparation, circuit execution, and repeated measurements. It also makes score quality depend strongly on how faithfully one generator state represents the background distribution. The benefit is therefore an architectural difference in scoring, not a complete end-to-end speedup claim.

# References

[[2023 - Quantum Generative Adversarial Networks For Anomaly Detection In High Energy Physics.pdf]]

[[2021 - Anomaly detection with variational quantum generative adversarial networks.pdf]]
