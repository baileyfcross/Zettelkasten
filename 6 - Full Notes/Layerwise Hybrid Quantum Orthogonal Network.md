2026-10-14 17:27

Status: #baby

Tags: [[Unary-Encoded Quantum Neural Networks]]

# Layerwise Hybrid Quantum Orthogonal Network

A multilayer [[Quantum Orthogonal Neural Network]] executes one orthogonal quantum layer at a time rather than concatenating every operation into one deep coherent circuit. After a pyramid transforms $|x\rangle$ into $|Wx\rangle$, tomography converts the amplitudes into a classical vector, a nonlinear activation is applied, and a new unary loader prepares the next layer's input.

This measurement-activation-reloading boundary supplies the nonlinearity that unitary evolution lacks and limits coherent circuit depth on noisy hardware. Its cost is repeated state preparation and [[Signed Unary-State Tomography]] between every pair of layers, so the architecture is modular but not an end-to-end quantum computation.

# References

[[2022 - Quantum Methods for Neural Networks and Application to Medical Image Classification.pdf]]
