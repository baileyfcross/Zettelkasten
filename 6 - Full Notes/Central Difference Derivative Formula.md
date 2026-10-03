2026-10-03 16:11

Status: #baby

Tags: [[Finite Difference Methods]]

# Central Difference Derivative Formula

For a smooth function on an equally spaced grid, the centered first-derivative approximation is

$$f'(x_i)\approx\frac{f(x_i+h)-f(x_i-h)}{2h}.$$

Its truncation error is of order $h^2$, one order better than the basic forward or backward quotient. The symmetry cancels even-power terms in the two Taylor expansions, but round-off and noisy data can still dominate when $h$ is too small.

# References

[[numericalmethodsinengineeringandscience.pdf]]

