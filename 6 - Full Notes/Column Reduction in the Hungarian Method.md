2026-10-03 22:06

Status: #baby

Tags: [[Assignment Optimization]]

# Column Reduction in the Hungarian Method

Column reduction subtracts the minimum entry of each column from every entry in that column after row reduction. It creates at least one zero per column without changing the identity of an optimal complete assignment.

Together, row and column reductions transform absolute costs into relative opportunities. The reduced matrix can then be searched for an [[Independent Zero Assignment]] covering every row and column.

# References

[[optimizationusinglinearprogramming.pdf]]

