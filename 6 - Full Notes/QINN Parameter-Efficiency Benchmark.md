2026-10-16 23:00

Status: #baby

Tags: [[Quantum Invertible Generative Models]]

# QINN Parameter-Efficiency Benchmark

The simulated QINN has roughly 2,000 trainable parameters, about 300 in quantum circuits and 1,700 in its classical inverse-state-preparation network. It is compared with spline-coupling INNs containing approximately 2,000, 6,000, and 16,000 parameters.

On the five-dimensional collider task, the QINN clearly exceeds the equal-sized classical model and is judged comparable to classical INNs with roughly three to eight times as many parameters. It reconstructs the sharp $Z$-mass peak better than the 16,000-parameter INN and uniquely captures the shown double peak in lepton separation, although the larger classical model fits distribution tails better.

This is model-capacity evidence, not a controlled resource advantage. The architectures allocate parameters differently, the QINN is mostly classical, and the experiment omits hardware measurements and total training cost, as emphasized by [[Cross-Architecture Parameter Count Limitation]].

# References

[[2023 - Generative Invertible Quantum Neural Networks.pdf]]

