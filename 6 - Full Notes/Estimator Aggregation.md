2026-09-29 19:17

Status: #baby

Tags: [[High-Dimensional Model Selection]]

# Estimator Aggregation

Estimator aggregation forms a weighted combination of candidate estimators instead of selecting exactly one. Convex weights can make the result more stable when several models have similar evidence, because a small perturbation need not switch the entire estimate from one candidate to another.

Selection is the special case that assigns weight one to a single estimator. Aggregation can retain comparable or sharper oracle guarantees, but computing weights over a huge model collection may be just as difficult as exhaustive selection. [[Gibbs Estimator Aggregation]] supplies one risk-controlled weighting rule.

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
