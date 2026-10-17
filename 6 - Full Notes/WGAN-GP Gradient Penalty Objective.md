2026-10-16 17:54

Status: #baby

Tags: [[Variational Quantum Wasserstein Anomaly Detection]]

# WGAN-GP Gradient Penalty Objective

A Wasserstein GAN replaces the discriminator probability of an ordinary GAN with an unbounded critic whose score estimates the separation between real and generated distributions. Its min-max objective is based on the 1-Wasserstein, or earth-mover, distance and requires the critic to behave as a 1-Lipschitz function.

WGAN-GP encourages that constraint by penalizing deviations of the critic-gradient norm from one. The penalty is evaluated at random points interpolated between real examples and generated examples. Training alternates several critic updates, which minimize the real-versus-generated score difference plus the penalty, with a generator update that tries to increase the critic's score on generated samples.

The interpolation penalty is a practical regularizer, not a proof that the critic is globally 1-Lipschitz. In the variational quantum implementation, the critic and its penalty remain entirely classical; only the generator block changes. This separation lets [[Hybrid Quantum-Classical QWGAN-GP Generator]] be compared with a classical generator under the same critic and loss.

# References

[[2021 - Anomaly detection with variational quantum generative adversarial networks.pdf]]
