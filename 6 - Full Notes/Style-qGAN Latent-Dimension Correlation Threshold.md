2026-10-16 22:03

Status: #baby

Tags: [[Style-qGAN Monte Carlo Event Generation]]

# Style-qGAN Latent-Dimension Correlation Threshold

In the three-dimensional Gaussian benchmark, the generator reproduces the sum of covariance eigenvalues to better than roughly 10% once the latent vector contains at least three independent dimensions. With fewer than three latent dimensions, the deviation is about an order of magnitude larger.

The result reflects an information bottleneck: repeated data reuploading can make a circuit more expressive, but it cannot manufacture enough independent random degrees of freedom to span a full-rank target distribution. Once the latent dimension reaches the target dimension, adding more coordinates produces little further improvement for this one-layer example.

This is an empirical threshold for a particular covariance matrix and ansatz, not a universal rule that latent dimension must always equal observable dimension. Deeper circuits, structured correlations, degenerate covariance, or different measurement maps can change the required dimension.

# References

[[2022 - Style-based quantum generative adversarial networks for Monte Carlo events.pdf]]

