2026-10-16 21:58

Status: #baby

Tags: [[Experimental Quantum GAN Image Generation]]

# Quantum Patch Sub-Generator Assembly

Each quantum patch sub-generator prepares a latent product state, applies a multilayer parameterized circuit, conditions on an ancillary subsystem, and measures the remaining feature register in the computational basis. The resulting basis probabilities become pixel values for one image patch, and the outputs of all sub-generators are concatenated into the complete sample.

The trainable circuit repeats layers of single-qubit rotations and fixed controlled-$Z$ entanglers between neighboring qubits. In the gray-scale-bar experiment, the circuit uses three qubits, three layers, and $R_Y$ rotations. In the handwritten-digit experiment, four five-qubit sub-generators with five layers each provide 100 generator parameters.

Every sub-generator receives the same [[Quantum Latent Rotation Encoding|latent state]] during an iteration. This coupling is important because independently sampled latent variables would not define one coherent generator map from $z$ to the assembled image. [[Quantum GAN Ancilla-Induced Nonlinearity]] explains why the conditioned probability vector is not merely a linear unitary transformation of the latent state.

# References

[[2021 - Experimental Quantum Generative Adversarial Networks for Image Generation.pdf]]
