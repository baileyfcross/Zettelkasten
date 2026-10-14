2026-10-14 17:55

Status: #baby

Tags: [[Variational Quantum Image Classification]]

# Classical Pretraining Burden of Variational Quantum Image Encoding

Approximate quantum image loading can move cost into classical preprocessing. The Fashion-MNIST pipeline optimizes a separate circuit for every one of 70,000 images, using up to 10,000 Adam epochs per state, and also trains all classifier configurations in classical simulation before hardware deployment.

Once the optimized QASM files exist, later experiments can reuse their shallow circuits and avoid repeating state-preparation search. However, an unseen image still requires a new classical optimization unless another loading rule is learned. The released circuit dataset is therefore valuable for controlled QML benchmarks while leaving open the practical problem of scalable on-demand encoding for data too large to simulate classically.

# References

[[2024 - Classification of the Fashion-MNIST Dataset on a Quantum Computer.pdf]]
