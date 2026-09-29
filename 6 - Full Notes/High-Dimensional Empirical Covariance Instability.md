2026-09-29 19:17

Status: #baby

Tags: [[High-Dimensional Statistical Foundations]]

# High-Dimensional Empirical Covariance Instability

The empirical covariance matrix is not a uniformly reliable approximation when dimension grows with sample size. Although each entry can converge to its population value, the spectrum of the whole matrix may remain badly distorted when $p$ is comparable to or larger than $n$.

For standardized independent Gaussian variables, the sample eigenvalues spread farther from one as $p/n$ increases. When $p>n$, the empirical covariance is singular. Procedures that invert it directly can therefore become unstable or impossible, motivating structural estimators such as the [[Graphical Lasso]] and low-rank or sparse covariance models.

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
