2026-10-15 10:16

Status: #baby

Tags: [[A-qGAN Anomaly Detection in High-Energy Physics]]

# A-qGAN Noise Robustness Evidence

The A-qGAN experiments compare noiseless simulation with a noise model calibrated to the superconducting `ibmq_belem` processor. The noisy optimization uses a larger learning rate and only one tenth as many epochs as the noiseless run. Across the three-to-eight-feature sweep, noisy and noiseless anomaly-detection AUC values remain broadly similar within substantial trial-to-trial variation.

This suggests that the shallow ansatze and local discriminator readout tolerate the modeled noise at the tested scale. It does not establish noise independence: overlapping error bands, altered optimization settings, limited features, and simulator assumptions make the evidence qualitative. Fidelity-based scoring can also face concentration even if gate noise remains manageable.

Actual hardware performance is lower in the separate three-feature Graviton experiment, where the AUC falls below both noiseless quantum simulation and the classical benchmark. Because that run also reduces training events and epochs, it cannot isolate the size of the hardware-noise penalty. Robustness claims should therefore be tested with matched training budgets and controlled noise ablations.

# References

[[2023 - Quantum Generative Adversarial Networks For Anomaly Detection In High Energy Physics.pdf]]
