2026-10-12 02:08

Status: #baby

Tags: [[Quantum Convolutional Neural Networks]]

# QCNN Convolution Layer

A QCNN convolution layer applies the same quasi-local unitary across a many-qubit input in a translationally invariant pattern. The unitary acts only on a bounded neighborhood, and repeated applications cover the active register at finite circuit depth.

Parameter sharing gives the layer a constant number of learned parameters independent of the total input size. This is the quantum analogue of a spatially shared [[Convolutional Kernel]], although the operation transforms a quantum state through unitary gates rather than computing weighted sums of classical pixels.

Several convolution layers may appear before each pooling step, and the sequence is repeated at successively smaller scales. The chosen locality, arrangement, and number of layers are fixed hyperparameters; the unitary parameters are learned from labeled quantum states or an error-correction objective.

# References

[[2019 - Quantum Convolutional Neural Networks.pdf]]
