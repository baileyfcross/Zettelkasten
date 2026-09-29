2026-09-29 19:17

Status: #baby

Tags: [[High-Dimensional Model Selection]]

# Gibbs Estimator Aggregation

Gibbs estimator aggregation weights each candidate by its prior weight multiplied by an exponential of negative estimated risk. The temperature parameter controls how sharply the mixture concentrates on the best-scoring models.

The resulting distribution minimizes estimated average risk plus a Kullback–Leibler penalty relative to the prior. Under the book's Gaussian regression conditions, the aggregate obtains an [[Oracle Risk Bound]] with leading constant one. Direct computation still requires summing over the model collection, so very large collections motivate [[Metropolis-Hastings Estimator Aggregation]].

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
