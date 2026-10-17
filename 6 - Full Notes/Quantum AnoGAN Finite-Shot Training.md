2026-10-16 17:54

Status: #baby

Tags: [[Variational Quantum Wasserstein Anomaly Detection]]

# Quantum AnoGAN Finite-Shot Training

Finite-shot training estimates the quantum generator's $Z$ expectations from sampled bitstrings and differentiates them with the parameter-shift rule. Compared with analytical state-vector expectations, sampling noise slows the rise of the fraud-detection F1 score as the optimizer needs more iterations to extract a stable direction.

With 100 or 500 shots per expectation, training eventually reaches approximately the same final F1 as the analytical simulation within the reported confidence intervals. A single shot performs much worse over the displayed training budget. Increasing shot count progressively makes the learning curve resemble the analytical result.

The finding separates convergence rate from final predictive quality: sampling noise need not lower the attainable score if enough optimization is performed, yet it can increase total circuit executions substantially. The simulation does not include realistic device noise, which the authors expect could further reduce convergence or final accuracy, so it is not a hardware-robustness result.

# References

[[2021 - Anomaly detection with variational quantum generative adversarial networks.pdf]]
