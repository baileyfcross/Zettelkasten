2026-10-16 22:46

Status: #baby

Tags: [[Quantum Generative Model Advantage Benchmarking]]

# Generative Model Benchmark Tuning Protocol

The race compares a QCBM, GRU-based RNN, decoder-only Transformer, variational autoencoder, and Wasserstein GAN. Each architecture receives a model-specific hyperparameter grid search, and the selected configuration is the one with the lowest utility after 100 training steps.

Every selected model then trains for 1,000 steps, is evaluated every 100 steps, and is repeated across ten random initializations on the same data for each training fraction. Matching iteration count creates a transparent training budget, but an iteration has different computational cost across CMA-ES, exact quantum simulation, autoregressive likelihood models, and adversarial networks.

Sampling used for intermediate evaluation is excluded from the track budgets, and training resources are effectively unrestricted. The protocol therefore controls data, nominal steps, and evaluation queries while leaving wall time, energy, hardware cost, and training-sample consumption outside the practical-advantage claim.

# References

[[2023 - A Framework for Demonstrating Practical Quantum Advantage Racing Quantum against Classical Generative Models.pdf]]

