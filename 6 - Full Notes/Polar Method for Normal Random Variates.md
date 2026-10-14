2026-10-07 17:18

Status: #baby

Tags: [[Pseudorandom Number Generation Methods]]

# Polar Method for Normal Random Variates

The polar method generates two candidate coordinates uniformly over a square, rejects pairs outside the unit disk or at its center, and transforms an accepted pair with a logarithmic radial factor. The result is a pair of independent standard normal values.

It is a rejection-based form of the [[Box-Muller Transform]] that avoids sine and cosine. The tradeoff is that some uniform pairs are discarded, so its cost depends on both the acceptance rate and the relative expense of the avoided trigonometric operations.

# References

[[statisticalcomputingincplusplusandr.pdf]]
