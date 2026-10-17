2026-10-16 22:03

Status: #baby

Tags: [[Style-qGAN Monte Carlo Event Generation]]

# Style-qGAN Hybrid Adversarial Training

Style-qGAN training alternates between a quantum generator and a classical discriminator. Reference data and generated samples train the discriminator to distinguish real from fake, while the discriminator's binary-cross-entropy signal updates the generator so its output becomes harder to reject.

The authors found a classical discriminator to converge faster than early all-quantum prototypes, so the discriminator remains a deep convolutional neural network. Both sides are optimized with ADADELTA, beginning with learning rates of $0.1$ for the discriminator and $0.5$ for the generator. Hyperparameters are manually tuned for each benchmark.

Simulation uses Qibo 0.1.6 with a TensorFlow backend. The resulting workflow demonstrates that a quantum circuit can serve as the generative component of a conventional adversarial loop, but it does not isolate whether performance gains come from quantum structure, additional trainable parameters, or optimization choices.

# References

[[2022 - Style-based quantum generative adversarial networks for Monte Carlo events.pdf]]

