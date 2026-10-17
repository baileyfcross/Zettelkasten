2026-10-16 21:58

Status: #baby

Tags: [[Experimental Quantum GAN Image Generation]]

# Quantum Batch GAN Register Partitioning

The quantum batch GAN partitions its qubits into an index register and a feature register. The index register coherently labels minibatch members. The feature register is further divided into data qubits plus ancillary qubits used to condition the generator and discriminator, so the generator and discriminator can each introduce the nonlinear normalization described by [[Quantum GAN Ancilla-Induced Nonlinearity]].

Latent vectors are prepared as a superposition $2^{-N_I/2}\sum_i|i\rangle|z_i\rangle$, and real examples use the analogous indexed state. The generator acts only on the appropriate feature subsystem, preserving the index. The discriminator then processes either the real or generated superposition and produces an averaged classification signal through a final measurement.

The partition exposes the architecture's resource tradeoff. Every extra index qubit doubles the nominal batch size but consumes a qubit that cannot represent features or ancillas. Preparing the indexed real and latent states may also require deep controlled operations, making [[Quantum GAN State-Preparation Bottleneck]] central to any scaling claim.

# References

[[2021 - Experimental Quantum Generative Adversarial Networks for Image Generation.pdf]]
