2026-10-07 17:18

Status: #baby

Tags: [[Pseudorandom Number Generation Methods]]

# Linear Congruential Generator

A linear congruential generator produces integer states by

$$x_i=(a x_{i-1}+c)\bmod m,$$

where the multiplier $a$, increment $c$, modulus $m$, and initial seed determine the entire sequence. Dividing a state by $m$ maps it into the unit interval for use as a pseudorandom uniform value.

Parameter choice determines the [[Random Number Generator Period]] and the lattice patterns among successive values. The recurrence is fast and reproducible, but poorly selected parameters can yield a short cycle and visibly dependent tuples.

# References

[[statisticalcomputingincplusplusandr.pdf]]
