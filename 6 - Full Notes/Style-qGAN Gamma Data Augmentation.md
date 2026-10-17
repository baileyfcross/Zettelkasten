2026-10-16 22:03

Status: #baby

Tags: [[Style-qGAN Monte Carlo Event Generation]]

# Style-qGAN Gamma Data Augmentation

A one-qubit, one-layer style-qGAN with one latent dimension and ten trainable parameters is trained on $10^4$ samples from a one-dimensional gamma distribution. The data are linearly mapped into $[-1,1]$ for quantum readout, the model trains in batches of 128 for $3\times10^4$ epochs, and generated values are transformed back to the original scale.

With 100 histogram bins, the KL divergence is $0.141$ for $10^4$ generated samples and $0.041$ for $10^5$ generated samples. Using $10^5$ samples and 1,000 bins raises it to $0.112$, showing how the apparent score depends on both sampling volume and bin resolution.

Generating ten times more samples than appear in the training set while preserving the distribution is presented as a data-augmentation test. It shows interpolation and distributional sampling in this controlled example, not the creation of new physical information or a general guarantee against GAN memorization.

# References

[[2022 - Style-based quantum generative adversarial networks for Monte Carlo events.pdf]]

