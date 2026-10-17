2026-10-16 17:54

Status: #baby

Tags: [[Variational Quantum Wasserstein Anomaly Detection]] · [[Experimental Quantum GAN Image Generation]]

# Hybrid Quantum Generator Gradient Estimation

Training the hybrid QWGAN-GP requires differentiating a classical critic loss through a classical upscaling layer and then through the quantum circuit's Pauli-$Z$ expectations. Ordinary automatic differentiation handles the critic and upscaler parameters, while circuit-parameter derivatives are supplied separately and combined by the chain rule.

For analytical state-vector expectations, the study uses forward differences. For shot-based expectations, it uses the parameter-shift rule: each trainable rotation angle is shifted by $\pm\pi/2$, and half the difference of the two expectation vectors gives the derivative. A minibatch Monte Carlo estimate over latent variables then supplies the generator-loss gradient used by Adam.

There are two distinct sampling layers in this calculation. The outer estimate samples latent inputs, while the inner estimate samples quantum measurement outcomes. Because the output observables in [[Commuting Z-Expectation Generator Readout]] share a measurement basis, a single bitstring batch supplies all of the inner expectations, although parameter shifts still require additional circuit evaluations.

The quantum patch GAN applies the same hybrid differentiation boundary to a different readout. Classical backpropagation updates its fully connected discriminator, while two generator-loss evaluations at shifts of $\pm\pi/2$ estimate each circuit-angle derivative. Its hardware experiments use 3,000 shots per probability or derivative estimate, linking the per-parameter circuit cost to the calibration described by [[Finite-Shot Quantum Generator Calibration]].

# References

[[2021 - Anomaly detection with variational quantum generative adversarial networks.pdf]]

[[2021 - Experimental Quantum Generative Adversarial Networks for Image Generation.pdf]]
