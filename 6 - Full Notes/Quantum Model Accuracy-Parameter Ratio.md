2026-10-15 00:05

Status: #baby

Tags: [[Quantum and Hybrid Convolutional Image Classification]]

# Quantum Model Accuracy-Parameter Ratio

An accuracy-parameter ratio compares validation accuracy with the number of trainable weights to highlight compact models. In the paper's selected configurations, HQNN-Parallel reached 74.8% with 15,658 parameters, while the purely quantum QCNN reached 42.5% with only 300. The structural classical baselines used 903,598 and 273,706 parameters, respectively, and the HQNN-Quanvolution model used 930,826 because most weights remained in its classical back end.

The QCNN consequently had the highest reported ratio even though it had much lower absolute accuracy. This metric captures parameter economy, not execution time, sample efficiency, memory traffic, gate count, or utility. Present-day circuit simulation was slower than classical training, and the experiments did not run on quantum hardware. A high ratio is therefore a prompt to study compactness, not evidence that the quantum model is computationally superior.

# References

[[2025 - Practical insights on the effect of different encodings ansatze and measurements in quantum and hybrid convolutional neural networks.pdf]]
