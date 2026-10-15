2026-10-15 10:16

Status: #baby

Tags: [[A-qGAN Anomaly Detection in High-Energy Physics]]

# A-qGAN HEP Benchmark Sampling Design

The A-qGAN benchmark starts from an artificial collider dataset containing more than 3.45 million Standard Model events for training and a similarly sized Standard Model test set. Separate simulated samples contain 139,991 Higgs events and 6,910 Graviton events. Every event is represented by 23 high-level features before [[A-qGAN PCA Angle-Encoding Pipeline|PCA compression]].

Quantum simulations draw 100 Standard Model training events and 100 events from each evaluation class. The matched classical benchmark uses 1,000 events from each dataset and includes the quantum subset. Ten random selections are evaluated so the reported means and standard deviations reflect sensitivity to resampling as well as model training.

This design intentionally probes small-data behavior rather than collider-scale throughput. It makes the quantum circuits simulable and tests whether a low-parameter qGAN can learn from fewer examples, but it does not reproduce the abundance of Standard Model data available in practice. Conclusions about sample efficiency must therefore remain distinct from claims about runtime, scaling, or deployment on the complete event stream.

# References

[[2023 - Quantum Generative Adversarial Networks For Anomaly Detection In High Energy Physics.pdf]]
