2026-10-16 21:58

Status: #baby

Tags: [[Experimental Quantum GAN Image Generation]]

# Quantum Patch GAN

A quantum patch GAN generates a high-dimensional classical sample by concatenating outputs from several small parameterized quantum circuits. Each sub-generator receives the same sampled latent state, produces a probability vector for one portion of the image, and is measured in the computational basis. The patched vector is then evaluated by a classical discriminator alongside real images.

The architecture lets a small quantum device address more output pixels than one circuit's feature register can expose at once. Its sub-generators can run sequentially on one processor or in parallel on distributed processors, and each can be tailored to the device's depth and connectivity. [[Quantum Patch Sub-Generator Assembly]] describes the mapping from circuit probabilities to pixels.

Patching does not eliminate resource growth: more image regions require more sub-generators, measurements, and trainable parameters. It can also weaken global image coherence because separate circuits model separate portions. The shared latent input supplies a common source of variation, and [[Quantum Patch GAN Convergence Guarantee]] shows that the combined generator retains the ideal GAN equilibrium under strong capacity and optimization assumptions.

# References

[[2021 - Experimental Quantum Generative Adversarial Networks for Image Generation.pdf]]
