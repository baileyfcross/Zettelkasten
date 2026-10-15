2026-10-15 10:16

Status: #baby

Tags: [[A-qGAN Anomaly Detection in High-Energy Physics]]

# qGAN Effective Dimension Capacity

Effective dimension estimates the fraction of a model's available function space that can be explored with its parameters. For a generator, a larger value indicates greater capacity to represent distinct distributions at the chosen parameter budget. Because the study matches quantum and classical generator parameter counts, it uses this measure to compare capacity per trainable parameter.

Across three to eight input features, the qGAN generator has a substantially larger empirical effective dimension than its classical counterpart. Both decline as feature count grows while parameter count remains linear, but the classical measure approaches zero more rapidly. The result suggests that the quantum ansatz uses a constrained parameter budget more expressively.

Effective dimension is not a performance guarantee. It does not show that the larger function family contains the correct background distribution, can be optimized reliably, generalizes better, or runs more cheaply. The evidence is therefore a capacity diagnostic consistent with possible advantage at larger dimension, not proof of quantum advantage. [[A-qGAN Feature-Count Performance Regimes]] supplies the corresponding task metrics on the small benchmark.

# References

[[2023 - Quantum Generative Adversarial Networks For Anomaly Detection In High Energy Physics.pdf]]
