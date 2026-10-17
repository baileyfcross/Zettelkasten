2026-10-16 17:54

Status: #baby

Tags: [[Variational Quantum Wasserstein Anomaly Detection]]

# Credit-Card Fraud AnoGAN Benchmark

The quantum AnoGAN benchmark uses 284,807 European credit-card transactions collected over 48 hours, including only 492 labeled frauds, or about 0.172 percent. The source data contain transaction amount, elapsed time, and 28 anonymized principal components. The experiment drops elapsed time, retains 29 features, and rescales each feature to $[0,1]$.

Adversarial training uses nonfraudulent transactions so the generator learns the ordinary-data distribution. Fraud labels enter later when the anomaly threshold and F1 score are evaluated. Because the positive class is extremely rare, the testing procedure oversamples frauds to form a set in which one quarter of examples are fraudulent; [[Oversampled F1 Evaluation for Fraud Detection]] describes the consequence.

The benchmark supports repeated controlled comparisons, but it is not a demanding demonstration of quantum expressivity. Even a classical generator consisting only of the final upscaling layer reaches a strong score. The resulting parity between classical and quantum models therefore shows functional feasibility, not that the variational circuit provides useful advantage on difficult anomaly structure.

# References

[[2021 - Anomaly detection with variational quantum generative adversarial networks.pdf]]
