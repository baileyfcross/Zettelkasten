2026-10-07 17:18

Status: #baby

Tags: [[Pseudorandom Number Generation Methods]]

# Tausworthe Generator

A Tausworthe generator builds a binary sequence from a linear recurrence modulo two and groups successive bits into pseudorandom fractions. Its state update can be implemented efficiently with bitwise shifts and exclusive-or operations.

The recurrence polynomial and initial bit state determine whether the sequence reaches its intended period. Tausworthe constructions avoid the integer multiplication of a [[Linear Congruential Generator]], but still require careful parameters and empirical testing of the resulting stream.

# References

[[statisticalcomputingincplusplusandr.pdf]]
