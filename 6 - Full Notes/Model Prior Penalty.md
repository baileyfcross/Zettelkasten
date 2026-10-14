2026-09-29 19:17

Status: #baby

Tags: [[High-Dimensional Model Selection]]

# Model Prior Penalty

A model prior penalty assigns candidate model $m$ a weight $\pi_m$ and penalizes it partly through $\log(1/\pi_m)$. Small prior weight represents greater combinatorial or substantive complexity, so a model must improve fit more strongly to be selected.

The weights need not express literal Bayesian belief; they can encode the number of models of a given size. This is crucial when exponentially many sparse supports share one dimension, because a penalty based only on dimension ignores the opportunity for an extreme noise fit. Proper weighting supports an [[Oracle Risk Bound]] across the whole collection.

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
