2026-10-03 22:06

Status: #baby

Tags: [[Simplex Algorithms and Basis Structure]]

# Simplex Pivot Operation

A simplex pivot exchanges one [[Nonbasic Variable]] for one [[Basic Variable]]. The pivot row is divided by the pivot element, then multiples of that row are removed from every other row so the entering column becomes a unit column.

The operation constructs a new adjacent basic solution without changing the represented constraints. Repeated pivots preserve feasibility when the [[Minimum Ratio Test]] selects the leaving variable correctly.

# References

[[optimizationusinglinearprogramming.pdf]]

