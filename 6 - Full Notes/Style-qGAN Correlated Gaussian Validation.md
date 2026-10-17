2026-10-16 22:03

Status: #baby

Tags: [[Style-qGAN Monte Carlo Event Generation]]

# Style-qGAN Correlated Gaussian Validation

The multivariate toy benchmark targets a zero-mean three-dimensional Gaussian whose covariance matrix contains both weak and strong off-diagonal correlations. A three-qubit, one-layer style-qGAN uses three latent dimensions, 34 trainable parameters, and two sequential controlled-$R_Y$ entanglers.

After training on $10^4$ samples for $1.3\times10^4$ epochs with batches of 128, the model generates $10^5$ samples. Marginal KL divergences are $0.015$, $0.045$, and $0.060$ for the three coordinates, and the two-dimensional projections reproduce the main correlation geometry while showing larger discrepancies in sparsely populated tails.

Covariance eigenvalues give a more direct correlation test than marginal histograms. Their relative errors fall below about 6% with $10^3$ generated samples, 1.3% with $5\times10^3$, and 0.8% with $2\times10^4$, demonstrating that finite sampling can dominate an otherwise accurate learned covariance.

# References

[[2022 - Style-based quantum generative adversarial networks for Monte Carlo events.pdf]]

