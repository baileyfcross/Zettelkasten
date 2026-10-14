2026-10-14 17:55

Status: #baby

Tags: [[Variational Quantum Image Classification]]

# Quantum Image Encoding Resource Tradeoff

Classical-data encodings redistribute rather than eliminate resource cost. Product encoding applies one shallow rotation per feature but needs one qubit per feature. General amplitude encoding uses logarithmically many qubits but can require circuit depth exponential in that qubit count. Data re-uploading allows width and depth to vary, yet still needs enough independent parameters to distinguish points in the original feature space.

For images, [[Flexible Representation of Quantum Images]] also compresses exponentially many pixel positions into linearly many qubits, while exact state preparation remains too deep for NISQ hardware. [[Variational FRQI State Preparation]] exploits image compressibility to produce shallow approximations, exchanging exactness and costly classical per-image optimization for lower compiled depth.

# References

[[2024 - Classification of the Fashion-MNIST Dataset on a Quantum Computer.pdf]]
