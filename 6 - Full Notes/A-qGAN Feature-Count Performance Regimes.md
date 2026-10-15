2026-10-15 10:16

Status: #baby

Tags: [[A-qGAN Anomaly Detection in High-Energy Physics]]

# A-qGAN Feature-Count Performance Regimes

The A-qGAN study varies the PCA-compressed input from three to eight features and finds that performance does not improve uniformly. Graviton detection becomes stronger as more components are added, with the quantum model reaching the classical ROC-AUC level at about six features and both methods plateauing thereafter.

Higgs detection is harder and follows a different pattern. The classical model is strongest with a small number of components and weakens after six, whereas the quantum simulations reach their best results at seven features. In the reported seven-feature comparison, qGAN and GAN metrics are broadly comparable despite their different training-set sizes.

This behavior shows that feature count is an empirical model-selection variable, not a simple proxy for information. Additional principal components may add useful signal, noise, or structure that one ansatz can represent better than another. The large run-to-run error bands also caution against selecting an architecture from a single training instance. [[A-qGAN Alpha and Threshold Selection]] adds a second layer of evaluation tuning after the feature dimension is chosen.

# References

[[2023 - Quantum Generative Adversarial Networks For Anomaly Detection In High Energy Physics.pdf]]
