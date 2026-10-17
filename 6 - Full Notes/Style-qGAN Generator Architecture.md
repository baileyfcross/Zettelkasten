2026-10-16 22:03

Status: #baby

Tags: [[Style-qGAN Monte Carlo Event Generation]]

# Style-qGAN Generator Architecture

The style-qGAN is a hybrid generative adversarial network whose generator is a parameterized quantum circuit and whose discriminator is a classical neural network. The generator begins in the computational-basis vacuum, applies repeated layers of single-qubit rotations and entangling gates, and ends with a final $R_Y$ layer before measurement.

Its defining architectural choice is [[Style-qGAN Latent Reuploading]]: latent variables enter throughout the circuit rather than only in an initial encoder. This repeated conditioning supplies each gate with both trainable parameters and random input while retaining a small qubit count. The authors call the model style-based by analogy to repeated latent injection in classical StyleGANs, but they do not use StyleGAN's learned latent-mapping network.

The implementation couples this generator to the workflow in [[Style-qGAN Hybrid Adversarial Training]]. It is a proof-of-concept generator for continuous distributions, not evidence that the sampled distributions are classically intractable or that the model provides quantum advantage.

# References

[[2022 - Style-based quantum generative adversarial networks for Monte Carlo events.pdf]]

