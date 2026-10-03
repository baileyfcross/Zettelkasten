2026-10-03 16:11

Status: #baby

Tags: [[Finite Difference Methods]]

# Finite Difference Error Propagation

An error in one tabulated entry spreads through every difference that depends on that entry. In higher-order columns, the error is multiplied by binomial coefficients with alternating signs.

Consequently, repeated differencing can magnify measurement or rounding noise even when the original table appears accurate. This sensitivity is one reason [[Numerical Differentiation]] from noisy data becomes less reliable at higher derivative orders.

# References

[[numericalmethodsinengineeringandscience.pdf]]

