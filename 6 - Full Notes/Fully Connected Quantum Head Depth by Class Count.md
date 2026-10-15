2026-10-15 00:05

Status: #baby

Tags: [[Quantum and Hybrid Convolutional Image Classification]]

# Fully Connected Quantum Head Depth by Class Count

Increasing the depth of the fully connected quantum head did not improve the four-class classifiers, where shallow models already reached their available operating range. For ten classes, deeper heads improved several configurations, and the training curves indicated that the purely quantum models were underparameterized rather than overfitting.

Every fully quantum model in the sweep had fewer than 400 trainable parameters. The class-count dependence shows why parameter additions should be tested against task capacity: more depth can be wasted when the decision problem is already expressible, yet useful when the output structure is more demanding. It also shows that simply adding weights is not always the right repair; for the four-class case, the authors conclude that changes to encoding, measurement, or architecture are more promising than a deeper copy of the same head.

# References

[[2025 - Practical insights on the effect of different encodings ansatze and measurements in quantum and hybrid convolutional neural networks.pdf]]
