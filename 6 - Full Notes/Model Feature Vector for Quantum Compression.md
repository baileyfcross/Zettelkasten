2026-10-12 01:33

Status: #baby

Tags: [[Enhanced Feature Quantum Autoencoders]]

# Model Feature Vector for Quantum Compression

A model feature vector supplies an enhanced feature quantum autoencoder with classical information that distinguishes members of a related family of quantum states. The vector is not the compressed quantum state itself; it is side information used to choose how the shared variational circuit acts on a particular input.

The feature should characterize a meaningful source of variation when one is available. In [[EF-QAE Ising Ground-State Compression]], the transverse field is used because it parameterizes the Hamiltonian and its ground states. In [[EF-QAE Handwritten-Digit Compression]], the class labels are represented by simple scalar values because the authors do not identify a more natural feature.

Conditioning the circuit this way turns one learned parameter set into a family of input-dependent transformations. The quality and representation of the feature vector therefore affect the optimization landscape and compression performance, and the paper leaves nonlinear encodings or freely optimized features as future possibilities.

# References

[[2021 - Quantum autoencoders with enhanced data encoding.pdf]]
