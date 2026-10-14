2026-10-14 17:55

Status: #baby

Tags: [[Variational Quantum Image Classification]]

# Classical Readout Contribution Audit

A classical readout contribution audit removes the trainable quantum classifier circuit and applies only the learned affine readout to measurements of the encoded input state. The resulting accuracy estimates how much predictive information the classical post-processing can extract without a learned quantum transformation.

On exactly FRQI-encoded Fashion-MNIST images, readout-only accuracy rises from 26.98% with two measured qubits to 60.11% with five of the eleven qubits. The [[Trainable Bitstring Observable Readout]] therefore carries substantial modeling power when it observes a large subsystem. Full variational circuits still achieve higher accuracy, but comparisons must attribute gains between the quantum transformation, the size of the measured subsystem, and the classical map rather than treating the hybrid model as entirely quantum.

# References

[[2024 - Classification of the Fashion-MNIST Dataset on a Quantum Computer.pdf]]
