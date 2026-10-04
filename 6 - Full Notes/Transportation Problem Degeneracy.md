2026-10-03 22:06

Status: #baby

Tags: [[Transportation and Transshipment Optimization]]

# Transportation Problem Degeneracy

A transportation basic feasible solution is degenerate when it has fewer than $m+n-1$ basic cells. This can occur during initial allocation or when several basic shipments reach zero at the same improvement step.

Degeneracy prevents all stepping-stone loops or MODI potentials from being determined. The repair is to place a symbolic very small allocation in an independent empty cell, preferably a low-cost one, until the basis has the required size without changing actual totals.

# References

[[optimizationusinglinearprogramming.pdf]]

