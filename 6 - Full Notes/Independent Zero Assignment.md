2026-10-03 22:06

Status: #baby

Tags: [[Assignment Optimization]]

# Independent Zero Assignment

An independent zero assignment selects zeros in a reduced cost matrix so no two selected zeros share a row or column. A full set of $n$ independent zeros directly specifies a feasible one-to-one assignment.

Rows or columns with a single available zero are handled first, and competing zeros are crossed out after a selection. If a complete set cannot be formed, the [[Minimum Zero Cover]] identifies how the matrix must be adjusted.

# References

[[optimizationusinglinearprogramming.pdf]]

