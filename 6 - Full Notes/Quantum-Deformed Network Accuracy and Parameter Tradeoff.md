2026-10-12 02:19

Status: #baby

Tags: [[Quantum-Deformed Probabilistic Neural Networks]]

# Quantum-Deformed Network Accuracy and Parameter Tradeoff

In the paper's dense ten-output model, the general two-gate deformation raised MNIST test accuracy from 91.1% to 94.3% and Fashion-MNIST accuracy from 84.2% to 86.8%. Its convolutional models gained roughly one percentage point or less because only their first convolutional layer was deformed.

These improvements came with many additional trainable parameters. The reported dense-layer parameterization used about 33 times as many parameters as the classical layer for the general deformation and about 17 times as many for the restricted variant. Translation-invariant versions sharply reduced that overhead but generally performed worse, and enlarged classical convolutional baselines sometimes matched or exceeded the deformed models.

The experiments therefore demonstrate modest gains for a classically simulated, quantum-inspired model rather than a controlled quantum advantage. Parameter count, the restriction to low entanglement, the absence of quantum-hardware execution, and the omission of batch normalization and pooling all limit what can be inferred from the headline accuracies.

# References

[[2020 - Quantum Deformed Neural Networks.pdf]]
