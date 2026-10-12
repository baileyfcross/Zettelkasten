2026-09-29 19:17

Status: #baby

Tags: [[High-Dimensional Statistical Foundations]]

# High-Dimensional Noise Accumulation

High-dimensional noise accumulation occurs when small coordinatewise errors combine into a large global error. If $p$ independent coordinates each have noise variance $\sigma^2$, the expected squared Euclidean noise is $p\sigma^2$.

The same scaling appears in orthonormal linear regression: the least-squares coefficient error grows with the number of fitted directions. Adding variables can therefore make an estimate increasingly unstable even when every individual measurement is precise. Structural assumptions such as sparsity or low rank reduce the number of directions in which noise must be estimated.

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
