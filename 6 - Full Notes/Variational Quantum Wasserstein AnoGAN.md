2026-10-16 17:54

Status: #baby

Tags: [[Variational Quantum Wasserstein Anomaly Detection]]

# Variational Quantum Wasserstein AnoGAN

A variational quantum Wasserstein AnoGAN trains a hybrid generator on normal data and then uses the learned model to score unusual inputs. The generator replaces the first neural-network block of a Wasserstein GAN with a parameterized quantum circuit, while the upscaling layer and critic remain classical. [[WGAN-GP Gradient Penalty Objective]] supplies the adversarial training signal.

The division of labor is deliberate. Random latent variables enter the quantum circuit, its measured expectations form a low-dimensional feature vector, and a classical layer maps that vector into the full data space. The high-dimensional training records therefore enter only the classical critic rather than requiring quantum state preparation. After training, [[AnoGAN Latent Variable Optimization]] searches for the generated point that best reconstructs each candidate transaction.

This architecture is a proof of principle rather than evidence of quantum advantage. On the reported fraud benchmark, quantum and classical versions reach similar final F1 scores, classical models converge faster at comparable depth, and the quantum circuit is simulated noiselessly. Its contribution is a concrete hybrid design that isolates quantum sampling in the generator while retaining conventional classical data handling.

# References

[[2021 - Anomaly detection with variational quantum generative adversarial networks.pdf]]
