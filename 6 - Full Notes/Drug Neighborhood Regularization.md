2026-09-28 03:43

Status: #baby

Tags: [[Pharmaceutical Discovery Analytics]]

# Drug Neighborhood Regularization

Drug neighborhood regularization encourages a drug's latent vector to remain close to those of its most similar drugs. Similarity weights form a directed nearest-neighbor graph, and the resulting penalty is added to the drug-target factorization objective.

Restricting the constraint to a small nearest neighborhood avoids forcing every weakly similar drug to influence the representation. The neighborhood size is therefore a bias-noise tradeoff that should be selected with validation data.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

