2026-10-07 17:18

Status: #baby

Tags: [[Pseudorandom Number Generation Methods]] [[SIMD Algorithm Reformulation Patterns]]

# Linear Congruential Generator

A linear congruential generator produces integer states by

$$x_i=(a x_{i-1}+c)\bmod m,$$

where the multiplier $a$, increment $c$, modulus $m$, and initial seed determine the entire sequence. Dividing a state by $m$ maps it into the unit interval for use as a pseudorandom uniform value.

Parameter choice determines the [[Random Number Generator Period]] and the lattice patterns among successive values. The recurrence is fast and reproducible, but poorly selected parameters can yield a short cycle and visibly dependent tuples.

Java's classic generator uses a 48-bit state, an odd increment, and a power-of-two modulus so masking replaces remainder. Its low bits have short regular periods, so `nextFloat` retains higher state bits. Although each state depends on its predecessor, expanding the affine recurrence yields $x_{n+k}=a^k x_n+c\sum_{i=0}^{k-1}a^i$, allowing prefix products and sums to generate several future states in parallel.

# References

[[statisticalcomputingincplusplusandr.pdf]]

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
