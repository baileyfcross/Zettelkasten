2026-10-16 23:00

Status: #baby

Tags: [[Quantum Invertible Generative Models]]

# Invertible QINN Angle Encoding

The QINN embeds one real-valued feature per qubit with a $Y$-axis rotation. Input features are first scaled into $[0,\pi]$, then passed through a trainable global affine transform whose parameters are clipped so the encoded angles remain in range.

This product-state preparation is invertible under the paper's rotation convention because each encoded angle can be recovered from the probability of measuring the corresponding qubit in state $|1\rangle$. The encoding therefore avoids the state-loading ambiguity that would arise from an arbitrary many-amplitude embedding.

The construction makes the qubit count equal to the feature dimension. It only solves inversion at the input boundary; after a trainable entangling circuit, the [[Quantum Measurement Inversion Problem]] still requires an additional learned mechanism.

# References

[[2023 - Generative Invertible Quantum Neural Networks.pdf]]

