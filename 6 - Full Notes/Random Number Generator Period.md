2026-10-07 17:18

Status: #baby

Tags: [[Pseudorandom Number Generation Methods]]

# Random Number Generator Period

The period of a pseudorandom generator is the number of state transitions before its deterministic state sequence repeats. No finite-state generator can avoid eventual repetition, so its usable stream must be short relative to a well-understood period.

A long period is necessary but not sufficient for useful simulation. Successive values can still show lattice structure or dependence, and parallel workers can accidentally consume overlapping subsequences unless streams are explicitly separated.

# References

[[statisticalcomputingincplusplusandr.pdf]]
