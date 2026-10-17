2026-10-16 22:51

Status: #baby

Tags: [[Style-qGAN Monte Carlo Event Generation]] · [[Quantum Generative Architecture Performance]]

# Style-qGAN Latent Reuploading

Standard quantum GAN generators commonly encode a latent vector once at the beginning of a circuit and then transform the resulting state with trainable gates. The style-qGAN instead injects latent coordinates into every single-qubit rotation and every entangling gate, making the random input available at every circuit layer.

Each injected gate uses the affine parameterization in [[Affine Latent Gate Encoding]]. Reusing latent variables in this way follows the data-reuploading intuition that repeated encoding enlarges the set of functions represented by a shallow circuit. [[Style-qGAN Feature-Map Inclusion]] formalizes the relation to a single-encoding generator.

Repeated injection should not be confused with increasing the dimension of the latent vector. The same latent coordinates can be reused many times, while [[Style-qGAN Latent-Dimension Correlation Threshold]] shows that too few independent coordinates can still prevent the generator from reproducing a target covariance structure.

A later continuous-generator benchmark uses a narrower form of the same idea: it injects the random vector through $R_X$ rotations at the start of every variational-entangling block. Unlike the style-qGAN, it does not make every trainable and entangling gate an affine function of the latent input. The comparison shows that data reuploading names a family of repeated-input circuits rather than one fixed gate parameterization.

# References

[[2022 - Style-based quantum generative adversarial networks for Monte Carlo events.pdf]]

[[2023 - A performance characterization of quantum generative models.pdf]]

