2026-10-16 21:58

Status: #baby

Tags: [[Experimental Quantum GAN Image Generation]]

# Quantum Patch GAN Handwritten-Digit Experiment

The hardware image experiment trains separate quantum patch GANs to generate handwritten zeros and ones from an optical-recognition dataset. Each example is an $8\times8$ gray-scale image. Four five-qubit sub-generators with five $R_Y$-and-controlled-$Z$ layers produce the 64 pixels, giving the quantum generator 100 trainable parameters.

Training uses a classical fully connected discriminator with hidden widths 64 and 16, approximately 350 adversarial iterations, and 3,000 measurement shots for circuit readout and generator-gradient estimation. The circuits run on adjacent qubits selected from a 12-transmon processor. Experimental samples visually resemble both the training images and samples from noiseless simulation.

The result demonstrates that a small superconducting processor can participate in end-to-end adversarial generation of recognizable real-world images. It is primarily qualitative: the paper does not report a distributional score for the digit data, because the dataset is limited and its underlying distribution is implicit. Quantitative comparison is instead performed by [[Quantum GAN Gray-Scale Bar Benchmark]].

# References

[[2021 - Experimental Quantum Generative Adversarial Networks for Image Generation.pdf]]
