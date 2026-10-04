2026-10-03 22:06

Status: #baby

Tags: [[Assignment Optimization]]

# Row Reduction in the Hungarian Method

Row reduction subtracts the smallest entry in each assignment-cost row from every entry in that row. This creates at least one zero per row while preserving which complete assignment has minimum total cost, because every feasible assignment uses exactly one entry from each row.

The resulting zeros represent pairings with no additional cost relative to that row's best option. [[Column Reduction in the Hungarian Method]] applies the same invariant across destinations.

# References

[[optimizationusinglinearprogramming.pdf]]

