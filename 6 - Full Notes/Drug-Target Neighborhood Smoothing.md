2026-09-28 03:43

Status: #baby

Tags: [[Pharmaceutical Discovery Analytics]]

# Drug-Target Neighborhood Smoothing

Drug-target neighborhood smoothing replaces an unreliable cold-start latent vector with a similarity-weighted combination of vectors from nearby entities that have known interactions. It can be applied to a new drug, a new target, or both before calculating the final logistic probability.

Smoothing occurs after training and differs from neighborhood regularization during training. It borrows an estimate for an unobserved row or column, but its quality depends on whether similarity neighbors genuinely share interaction behavior.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

