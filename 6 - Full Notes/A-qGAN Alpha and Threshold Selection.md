2026-10-15 10:16

Status: #baby

Tags: [[A-qGAN Anomaly Detection in High-Energy Physics]]

# A-qGAN Alpha and Threshold Selection

An A-qGAN detector requires two decisions after the generative model has been trained. The coefficient $\alpha$ determines the balance between generator-state fidelity and discriminator response in the anomaly score, while a threshold $\delta$ turns the continuous score into an anomalous or non-anomalous label.

The study performs a grid search over $\alpha$ and selects the value that maximizes ROC-AUC on the evaluation data. Dataset-level score means are then used to define thresholds that separate Standard Model events from the chosen Higgs or Graviton anomaly sample. Accuracy, precision, F1, and ROC-AUC are reported at the selected setting.

This procedure is appropriate for benchmarking known held-out classes, but it introduces supervised information into calibration even though the underlying qGAN was trained only on background. A deployment intended to discover unknown physics cannot tune against the anomaly it hopes to find. It must set operating thresholds from background-only validation, injected synthetic signals, sidebands, or a prespecified false-positive budget and then test them on untouched data.

# References

[[2023 - Quantum Generative Adversarial Networks For Anomaly Detection In High Energy Physics.pdf]]
