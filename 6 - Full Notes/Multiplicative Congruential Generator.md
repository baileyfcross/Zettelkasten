2026-10-07 17:18

Status: #baby

Tags: [[Pseudorandom Number Generation Methods]]

# Multiplicative Congruential Generator

A multiplicative congruential generator is a [[Linear Congruential Generator]] whose increment is zero:

$$x_i=a x_{i-1}\bmod m.$$

The seed must be chosen from the nonzero states that participate in the intended cycle because zero remains zero forever. Suitable multipliers and moduli can produce a long period, but successive tuples still occupy a lattice structure rather than filling space as independent random points would.

# References

[[statisticalcomputingincplusplusandr.pdf]]
