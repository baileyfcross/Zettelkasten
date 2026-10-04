2026-10-03 22:06

Status: #baby

Tags: [[Transportation and Transshipment Optimization]]

# Northwest Corner Method

The northwest corner method begins at the upper-left cell of a balanced transportation tableau and allocates the smaller of the row's remaining supply and the column's remaining demand. It then crosses out the exhausted row or column and repeats at the new northwest corner.

The rule is mechanical and does not use shipping costs, so it supplies feasibility rather than a good objective value. If a row and column are exhausted together, a zero basic allocation may be needed to retain $m+n-1$ basic cells.

# References

[[optimizationusinglinearprogramming.pdf]]

