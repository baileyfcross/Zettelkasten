2026-10-12 02:08

Status: #baby

Tags: [[Quantum Convolutional Neural Networks]]

# QCNN Symmetry-Protected Phase Recognition

The paper applies a QCNN to recognize a one-dimensional symmetry-protected topological phase in a spin chain. An exact circuit uses controlled-phase and Toffoli operations in its convolution layers, measurement-conditioned phase corrections in pooling, and a final measurement related to the cluster-state stabilizer.

Increasing circuit depth sharpens the output near the phase boundary. Matrix-product-state simulations show that a depth-two exact circuit already reproduces the phase diagram accurately, and a related isometric mapping lets the same construction identify the Haldane-chain transition.

The authors also train a depth-one, 15-spin model with 1,309 parameters on 40 points from an exactly solvable line. Its output generalizes across the two-dimensional parameter region, including a phase boundary not crossed by the training line. This is numerical evidence for the architecture on the studied Hamiltonian, not a hardware demonstration or a guarantee for arbitrary quantum phases.

# References

[[2019 - Quantum Convolutional Neural Networks.pdf]]
