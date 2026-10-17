2026-10-16 23:13

Status: #baby

Tags: [[Quantum State Diffusion Models]]

# Quantum Scrambling Forward Diffusion

Quantum scrambling forward diffusion gradually transforms each sampled target state into an approximately random pure state. At every diffusion step, the construction independently samples a unitary for each data state, producing a sequence of ensembles from the original distribution toward Haar-like noise.

The implemented fast-scrambling layer combines arbitrary single-qubit rotations with homogeneous all-to-all $ZZ$ rotations. Adjusting the random-angle ranges controls how quickly information about the initial ensemble spreads through Hilbert space.

This process supplies both the terminal noise distribution and the intermediate training targets for [[Sequential QuDDPM Training Cycles]]. It is an actual component of the generative algorithm, not merely a theoretical analogy used to analyze circuit randomness.

# References

[[2023 - Generative quantum machine learning via denoising diffusion probabilistic models.pdf]]

