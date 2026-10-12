2026-10-07 17:18

Status: #baby

Tags: [[Pseudorandom Number Generation Methods]]

# Lehmer Random Number Generator

A Lehmer random number generator is a [[Multiplicative Congruential Generator]] designed around a carefully selected modulus and multiplier. Starting from a nonzero seed, it repeatedly multiplies the state and reduces it modulo the chosen integer.

Implementations must avoid arithmetic overflow before the modular reduction. The book demonstrates quotient-and-remainder rearrangements that compute the same recurrence while keeping intermediate integer values within the machine range.

# References

[[statisticalcomputingincplusplusandr.pdf]]
