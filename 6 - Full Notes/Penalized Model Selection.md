2026-09-29 19:17

Status: #baby

Tags: [[High-Dimensional Model Selection]]

# Penalized Model Selection

Penalized model selection chooses the model minimizing a lack-of-fit term plus a complexity penalty. In Gaussian regression, residual sum of squares favors larger subspaces, while the penalty counters the extra variance and the chance that one model looks unusually good only through noise.

Dimension alone can be insufficient when the number of models grows rapidly with dimension. A useful penalty must reflect both model size and multiplicity, often through a [[Model Prior Penalty]]. The goal is not necessarily to identify a true model but to approach the prediction risk of the [[Oracle Estimator]].

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
