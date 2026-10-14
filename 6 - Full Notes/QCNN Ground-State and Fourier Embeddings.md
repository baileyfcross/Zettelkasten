2026-10-14 09:01

Status: #baby

Tags: [[Quantum Convolutional Neural Networks]]

# QCNN Ground-State and Fourier Embeddings

A rotation-based feature map encodes a scalar through gates such as $R_y(\eta x)$, producing Fourier-like basis functions whose accessible frequencies are controlled by the scale $\eta$. Low-frequency versions can represent the cluster-phase boundary, but raising the frequency range introduces oscillatory basis functions that make the boundary harder to learn from sparse data.

In the paper's comparison, models with $\eta=2$ or $4$ reach perfect classification accuracy, while the higher-frequency $\eta=8$ model produces an oscillatory output and reaches 65 percent. Choosing a suitable Fourier bandwidth is therefore a feature-engineering decision rather than an automatic consequence of the QCNN architecture.

The ground-state embedding instead supplies basis functions that already change sharply at the physical critical point. This alignment produces the inductive bias described by [[Ground-State Embedding Basis Functions]] and the sampling behavior in [[QCNN Finite-Shot Generalization]]. The comparison does not claim that Fourier embeddings are universally inferior; it shows that a problem-matched physical embedding can reduce the burden on training and measurement.

# References

[[2023 - What can we learn from quantum convolutional neural networks.pdf]]
