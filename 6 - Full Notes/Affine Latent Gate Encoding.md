2026-10-16 22:03

Status: #baby

Tags: [[Style-qGAN Monte Carlo Event Generation]]

# Affine Latent Gate Encoding

Each style-qGAN rotation angle is an affine function of a latent coordinate. For a gate in layer $l$, the angle has the form $\phi_g^{(l)}z^{(m)}+\phi_g^{(l-1)}$, so one trainable coefficient scales the selected latent variable and another acts as a bias.

This weight-and-bias interpretation makes a quantum gate resemble a classical neuron whose activation is supplied by the unitary rotation. The same principle is applied to both the alternating $R_Y$ and $R_Z$ rotations and the parameterized entangling operations, so [[Style-qGAN Latent Reuploading]] conditions local and correlation-building transformations alike.

Because each encoded gate introduces two trainable values rather than one unconstrained angle, the style-qGAN baseline contains more parameters than a standard circuit with the same qubit count and number of layers. [[Style-qGAN Standard-Architecture Comparison]] therefore controls circuit shape but cannot simultaneously equalize parameter count without changing the standard architecture.

# References

[[2022 - Style-based quantum generative adversarial networks for Monte Carlo events.pdf]]

