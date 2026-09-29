2026-09-29 19:17

Status: #baby

Tags: [[High-Dimensional Model Selection]]

# Scale-Invariant Estimation

A scale-invariant estimator transforms proportionally when the response is multiplied by a positive constant. Its tuning rule therefore does not need to know the unknown response or noise scale merely to preserve the same fitted structure.

Ordinary Lasso tuning depends on noise variance, while the [[Square-Root Lasso]] changes the loss so a theoretically useful penalty can be chosen independently of that variance. Scale invariance solves only one part of selection: the oracle tuning value can still depend on the unknown signal, so data-driven tuning or estimator comparison remains useful.

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
