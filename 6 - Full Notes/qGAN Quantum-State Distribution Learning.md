2026-10-15 10:16

Status: #baby

Tags: [[A-qGAN Anomaly Detection in High-Energy Physics]]

# qGAN Quantum-State Distribution Learning

A quantum generative adversarial network can represent a classical data distribution through quantum states. Each training vector $x_i$ is embedded as $|x_i\rangle$, while a parameterized generator prepares a single state $|G\rangle=G(\theta_G)|0\rangle^{\otimes n}$ intended to represent the full distribution. Measurements of that state produce samples that can be mapped back into the feature space.

The discriminator receives either the generator state or an embedded training state and classifies it by measuring Pauli $Z$ on its final qubit. Its expectation value is converted into a probability of labeling the input as real. Alternating gradient updates make the generator increase that probability while the discriminator increases the difference between its responses to data and generated input.

This is not a point-for-point reconstruction objective. The generator learns a quantum representation whose measurement statistics resemble the background process, which can then serve as the reference in the [[Anomaly qGAN Framework]]. Because the generator supplies one state while the discriminator sees batches of individual data states, [[A-qGAN Adversarial Update Scheduling]] is needed to limit training bias.

# References

[[2023 - Quantum Generative Adversarial Networks For Anomaly Detection In High Energy Physics.pdf]]
