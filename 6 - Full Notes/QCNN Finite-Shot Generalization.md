2026-10-14 09:01

Status: #baby

Tags: [[Quantum Convolutional Neural Networks]]

# QCNN Finite-Shot Generalization

Finite-shot error in a QCNN expectation estimate scales with the observable's variance divided by the number of measurements. The location and width of high-variance regions therefore affect how reliably a trained decision boundary can be sampled, even when its infinite-shot prediction is accurate.

For the paper's ground-state embedding, high variance is concentrated in a narrow neighborhood of the phase transition. The rotation-based Fourier embedding has a much broader uncertain region, so test points far from criticality remain vulnerable to sampling error. Across repeated trials, the ground-state model recovers 100 percent classification accuracy with 100 shots, while the Fourier model requires 10,000 shots to approach its 99.6 percent infinite-shot accuracy.

The advantage persists when shot noise is included during both training and testing. With 200 shots per expectation estimate, the ground-state model retains a sharp transition and 100 percent test accuracy, whereas the Fourier model is noisy around the critical region and reaches 97 percent. This is an embedding-dependent sampling result rather than a guarantee for every QCNN or dataset.

# References

[[2023 - What can we learn from quantum convolutional neural networks.pdf]]
