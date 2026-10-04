2026-10-03 22:06

Status: #baby

Tags: [[Assignment Optimization]]

# Assignment as a Transportation Model

An assignment problem is a transportation model with the same number of origins and destinations, unit supply at every origin, and unit demand at every destination. Binary variables ensure that each origin is paired with exactly one destination and vice versa.

A direct transportation basis would be highly degenerate because only $n$ of the $2n-1$ basic variables carry value one. The [[Hungarian Method]] exploits this one-to-one structure instead of using a general transportation algorithm.

# References

[[optimizationusinglinearprogramming.pdf]]

