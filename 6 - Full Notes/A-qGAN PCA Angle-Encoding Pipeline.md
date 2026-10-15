2026-10-15 10:16

Status: #baby

Tags: [[A-qGAN Anomaly Detection in High-Energy Physics]]

# A-qGAN PCA Angle-Encoding Pipeline

The A-qGAN experiment begins with collision events described by 23 high-level classical features. Principal component analysis compresses them to between three and eight components, and the training values are rescaled to $[-\pi/2,\pi/2]$ so they fit the periodic range of the circuit's rotation gates.

Each $n$-component vector is then angle encoded into an $n$-qubit product state by applying $R_Y(x_i)$ to qubit $i$. This mapping uses one qubit per retained principal component and has a shallow preparation circuit, making it practical for the small hardware experiment. Entanglement is introduced later by the generator and discriminator ansatze rather than by the input map itself.

The pipeline makes the experiment feasible while limiting what its quantum stage can access. PCA is linear and chooses directions of variance without optimizing specifically for anomaly separation; discarding components can remove rare-signal structure, and classical preprocessing can erase quantum correlations that might exist in a future quantum-native detector. Results therefore describe an A-qGAN operating on compressed classical features, not directly on raw collider or quantum-sensor data.

# References

[[2023 - Quantum Generative Adversarial Networks For Anomaly Detection In High Energy Physics.pdf]]
