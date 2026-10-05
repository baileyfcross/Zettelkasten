2026-10-04 22:20

Status: #baby

Tags: [[R Data Transformation and Reshaping]]

# R Split-Apply-Combine

R split-apply-combine divides a vector or data frame by one or more grouping variables, applies the same function to each subset, and recombines the results into a named collection or table. The grouping definition determines the unit of comparison, while the return shape of the function determines how easily the pieces can be combined.

This pattern supports group summaries without manually creating one object per category. Empty groups, unused factor levels, and missing group values must be considered because they can alter which subsets appear in the result.

# References

[[rprimer.pdf]]
