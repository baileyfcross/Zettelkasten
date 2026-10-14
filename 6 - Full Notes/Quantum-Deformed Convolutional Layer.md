2026-10-12 02:19

Status: #baby

Tags: [[Quantum-Deformed Probabilistic Neural Networks]]

# Quantum-Deformed Convolutional Layer

A quantum-deformed convolutional layer applies the same quantum-deformed binary-layer calculation to each local image patch covered by a [[Convolutional Kernel]]. The activation and weight qubits for a patch are correlated by a deformation circuit, and their thresholded output is evaluated with the same phase-estimation construction used for a dense layer.

Using a shared deformation for each translated patch preserves the translation equivariance of a [[Convolutional Neural Network]]. In the paper's classical experiments, computational cost limited deformation to the first convolutional layer, while later convolutional and dense layers used the undeformed probabilistic binary construction.

The reported convolutional gains were generally about one percentage point or less and shrank relative to stronger, parameter-matched classical baselines. This distinguishes the design from a generic quantum convolutional architecture and keeps its empirical claim narrower than [[Quantum-Deformed Sampling Speedup]].

# References

[[2020 - Quantum Deformed Neural Networks.pdf]]
