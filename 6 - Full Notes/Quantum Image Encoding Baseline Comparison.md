2026-10-14 17:55

Status: #baby

Tags: [[Variational Quantum Image Classification]]

# Quantum Image Encoding Baseline Comparison

The paper compares exactly prepared Fashion-MNIST states under direct amplitude encoding, [[Flexible Representation of Quantum Images|FRQI]], and Novel Enhanced Quantum Representation (NEQR). Sequential variational classifiers give similar accuracy for amplitude and FRQI encodings, with FRQI slightly higher at the cost of one extra qubit.

NEQR stores each quantized pixel value in one to three color qubits rather than a rotation amplitude. In these experiments it needs more qubits and produces substantially lower accuracy across comparable classifier CNOT counts. The result is specific to the chosen circuits and dataset, but it supports FRQI as a practical compromise between compact representation, image-state compressibility, and downstream classification performance.

# References

[[2024 - Classification of the Fashion-MNIST Dataset on a Quantum Computer.pdf]]
