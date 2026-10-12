2026-10-07 17:18

Status: #baby

Tags: [[Pseudorandom Number Generation Methods]]

# Inverse Transform Sampling

Inverse transform sampling converts a uniform random value $U$ into a draw from a target distribution by applying its quantile function:

$$X=F^{-1}(U).$$

The method is direct when the cumulative distribution function has a tractable inverse, as with the exponential distribution. If the inverse is unavailable in closed form, it may be evaluated numerically; if even the cumulative distribution is difficult to compute, [[Rejection Sampling]] can be more practical.

# References

[[statisticalcomputingincplusplusandr.pdf]]
