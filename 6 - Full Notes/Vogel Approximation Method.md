2026-10-03 22:06

Status: #baby

Tags: [[Transportation and Transshipment Optimization]]

# Vogel Approximation Method

Vogel's approximation method computes a penalty for every active row and column: the difference between its two smallest unit costs. It selects the largest penalty, allocates as much as possible to that row or column's lowest-cost cell, and then recomputes penalties after an exhaustion.

The penalty estimates the opportunity cost of losing the cheapest route. The method generally produces an optimal or near-optimal starting plan, but its result still needs verification with the [[Stepping-Stone Method]] or [[MODI Method]].

# References

[[optimizationusinglinearprogramming.pdf]]

