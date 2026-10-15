2026-10-15 00:05

Status: #baby

Tags: [[Quantum and Hybrid Convolutional Image Classification]]

# Structural-Twin Baseline for Hybrid Quantum Networks

A structural-twin baseline isolates a hybrid network's quantum component by replacing it with a classical layer of comparable input-output role while leaving the rest of the model and training procedure unchanged. The HQNN-Parallel baseline bypasses the quantum branch with a multilayer perceptron, while the HQNN-Quanvolution baseline replaces the initial patch circuits with a classical convolution having matched spatial reduction.

Both variants use the same optimizer settings, dataset split, and surrounding architecture as their hybrid counterparts. This controls more variables than comparing against an unrelated high-performing network and helps attribute differences to the substituted layer. It is not a state-of-the-art benchmark: the baselines are architectural references, not heavily tuned EuroSAT systems. A hybrid improvement over such a twin is therefore evidence about that component under fixed conditions, not evidence of quantum utility or superiority over modern pretrained vision models.

# References

[[2025 - Practical insights on the effect of different encodings ansatze and measurements in quantum and hybrid convolutional neural networks.pdf]]
