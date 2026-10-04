2026-10-03 22:06

Status: #baby

Tags: [[Assignment Optimization]]

# Hungarian Matrix Adjustment

When a reduced assignment matrix lacks enough independent zeros, the smallest uncovered entry is subtracted from every uncovered cell and added to cells at intersections of covering lines. Cells covered by one line remain unchanged.

This transformation creates additional zeros while preserving optimal assignments under the Hungarian method's cost invariants. Reduction, zero assignment, covering, and adjustment repeat until one independent zero can be chosen in every row and column.

# References

[[optimizationusinglinearprogramming.pdf]]

