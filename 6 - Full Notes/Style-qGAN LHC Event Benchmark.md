2026-10-16 22:03

Status: #baby

Tags: [[Style-qGAN Monte Carlo Event Generation]]

# Style-qGAN LHC Event Benchmark

The simulated LHC model uses three qubits, five latent dimensions, two variational layers, 62 trainable parameters, and two sequential controlled-$R_Y$ entanglers. It trains on $10^4$ transformed events for $3\times10^4$ epochs with batches of 128, then generates $10^5$ events in noiseless simulation.

The generated marginals achieve KL divergences of $0.064$ for $s$, $0.074$ for $t$, and $0.050$ for $y$. Two-dimensional projections reproduce the main kinematic correlations, although ratio plots reveal discrepancies in sparse boundaries and tails that marginal scores alone would hide.

The sum of covariance eigenvalues differs from the reference by roughly 7–15% over generated samples ranging from $10^3$ to $2\times10^4$. The authors attribute much of this variation to the limited reference subsamples, so the benchmark supports approximate correlation learning rather than precision-event generation.

# References

[[2022 - Style-based quantum generative adversarial networks for Monte Carlo events.pdf]]

