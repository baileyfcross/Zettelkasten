2026-10-16 23:00

Status: #baby

Tags: [[Quantum Invertible Generative Models]]

# Reconstruction MSE Invertibility Loss

Reconstruction MSE trains a QINN for functional invertibility by penalizing the squared difference between an input $x$ and its round-trip reconstruction $\tilde x$:

$$L_{\mathrm{MSE}}=\lambda_{\mathrm{MSE}}\lVert x-\tilde x\rVert^2.$$

The round trip measures the forward circuit, rebuilds a state with [[Learnable Hybrid Inverse State Preparation]], applies the adjoint main circuit, and decodes the recovered input. Unlike a fidelity loss, MSE does not demand that the reconstructed premeasurement state equal the original state; it only demands the same inverse output.

That freedom matches the actual bijection requirement and performed better in the paper's experiment. The MSE-trained QINN preserved the reconstructed mass peak without the pronounced separation artifacts produced by the stricter state-fidelity objective.

# References

[[2023 - Generative Invertible Quantum Neural Networks.pdf]]

