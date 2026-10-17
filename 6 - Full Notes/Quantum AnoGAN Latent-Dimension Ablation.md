2026-10-16 17:54

Status: #baby

Tags: [[Variational Quantum Wasserstein Anomaly Detection]]

# Quantum AnoGAN Latent-Dimension Ablation

Changing the quantum generator's qubit count, or the classical generator's latent width, produces only small changes in final fraud-detection F1. The quantum mean is slightly higher at five and six latent dimensions, but its 95 percent confidence intervals overlap the classical result. The dataset therefore appears describable by a small number of latent variables.

A random-forest feature ranking supports that interpretation: the three most important features account for roughly $0.4$ of joint mean decrease impurity and the six most important for roughly $0.6$. Restricting the data to those six features lets the experiment remove the classical upscaling layer and compare six-output generators directly.

Without upscaling, a shallow six-qubit generator remains competitive, while the comparable classical generator becomes slightly worse than the all-feature architecture. This is a useful ablation of the hybrid design, but feature selection is supervised by a classical importance model and the uncertainty bands do not establish a quantum advantage.

# References

[[2021 - Anomaly detection with variational quantum generative adversarial networks.pdf]]
