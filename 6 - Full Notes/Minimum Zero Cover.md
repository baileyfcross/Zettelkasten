2026-10-03 22:06

Status: #baby

Tags: [[Assignment Optimization]]

# Minimum Zero Cover

The minimum zero cover is the smallest collection of horizontal and vertical lines that covers all zeros in a reduced assignment matrix. In the Hungarian procedure, fewer than $n$ covering lines means the current zeros cannot support a complete independent assignment.

The cover is constructed by marking unassigned rows, columns containing crossed zeros in those rows, and rows containing assignments in those columns. Covered and uncovered positions then guide the [[Hungarian Matrix Adjustment]].

# References

[[optimizationusinglinearprogramming.pdf]]

