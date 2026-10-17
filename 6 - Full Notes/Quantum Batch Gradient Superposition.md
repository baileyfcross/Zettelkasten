2026-10-16 21:58

Status: #baby

Tags: [[Experimental Quantum GAN Image Generation]]

# Quantum Batch Gradient Superposition

The proposed batch qGAN encodes $2^{N_I}$ examples under $N_I$ index qubits and applies the same generator and discriminator circuits coherently across them. A measurement of the discriminator output estimates the average real-or-fake response over the indexed batch, which can be inserted into the adversarial loss and its parameter gradients.

This construction aims to replace a classical sum of per-example gradients with one coherent circuit process. Because the discriminator performs binary classification, its averaged output can in principle be read from one qubit, and the number of measured observables need not grow with batch size. Finite shots still determine the statistical precision of that average.

The speedup is conditional. Exact preparation of the indexed data state can cost as much asymptotically as loading the classical dataset, and the experiment uses no index qubits, so the parallel-gradient claim is theoretical. It becomes meaningful only if the required oracles are prepared cheaply enough and if circuit depth, postselection, and shot complexity remain controlled.

# References

[[2021 - Experimental Quantum Generative Adversarial Networks for Image Generation.pdf]]
