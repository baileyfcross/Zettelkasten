2026-10-14 09:01

Status: #baby

Tags: [[Quantum Convolutional Neural Networks]]

# QCNN Ground-State Regression

The sharp basis functions of a ground-state embedding can support regression targets with rapid transitions, not only binary phase labels. The paper trains a QCNN expectation value, with an additional affine rescaling, as a surrogate for functions drawn from fluid dynamics and wave physics.

For a viscous Burgers-equation profile with a shock-like change, the model is trained on 21 evenly spaced points and evaluated on 100 test points. Using a squared-error threshold of 0.05, the ground-state embedding reaches 91 percent test accuracy compared with 62 percent for the rotation-based Fourier embedding.

For a damped-oscillator transfer function, both embeddings reproduce the central resonance, but the ground-state model better follows the endpoint behavior and scores 100 percent compared with 91 percent for the Fourier model. These numerical examples support a transfer-learning interpretation: a Hamiltonian's critical basis can be reused for nonquantum target functions with a compatible shape, rather than providing a general-purpose regression advantage.

# References

[[2023 - What can we learn from quantum convolutional neural networks.pdf]]
