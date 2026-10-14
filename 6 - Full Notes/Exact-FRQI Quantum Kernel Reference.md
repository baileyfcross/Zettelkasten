2026-10-14 17:55

Status: #baby

Tags: [[Variational Quantum Image Classification]]

# Exact-FRQI Quantum Kernel Reference

The paper uses a support-vector classifier with kernel $K(x,x')=\langle\psi(x)|\psi(x')\rangle^2$ on exactly prepared real FRQI state vectors. A quadratic polynomial SVM with one-versus-rest multiclass handling and regularization $C=1000$ reaches 89.48% test accuracy.

For a fixed feature map, the representer theorem makes the kernel solution a useful reference for training accuracy, while a restricted variational circuit may generalize differently. Here the kernel score is not a hardware result: exact state vectors and kernel values are evaluated classically. It provides a ceiling-like comparison for the chosen FRQI representation, not evidence of a quantum computational advantage.

# References

[[2024 - Classification of the Fashion-MNIST Dataset on a Quantum Computer.pdf]]
