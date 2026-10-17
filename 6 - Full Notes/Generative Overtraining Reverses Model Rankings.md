2026-10-16 22:46

Status: #baby

Tags: [[Quantum Generative Model Advantage Benchmarking]]

# Generative Overtraining Reverses Model Rankings

More optimization steps do not monotonically improve generalization. In the larger-data T1 experiment, the RNN and Transformer quickly discover low-cost unseen samples, then their minimum values and utilities worsen as training continues and the models fit the reweighted training distribution more closely.

The QCBM's utility decreases more steadily, while the VAE and WGAN retain strong best-value performance. Because the winning checkpoint can occur well before the common 1,000-step endpoint, reporting only final metrics can reverse the apparent ranking of otherwise identical runs.

Early stopping must therefore be a predeclared part of the benchmark rather than a post hoc choice made only for a favored model. Monitoring the same metrics at the same checkpoints, as in [[Generative Model Benchmark Tuning Protocol]], makes checkpoint selection comparable across architectures.

# References

[[2023 - A Framework for Demonstrating Practical Quantum Advantage Racing Quantum against Classical Generative Models.pdf]]

