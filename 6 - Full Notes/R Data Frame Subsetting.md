2026-10-04 22:20

Status: #baby

Tags: [[R Data Transformation and Reshaping]]

# R Data Frame Subsetting

R data frame subsetting selects rows, columns, or both by position, name, or logical condition. Because a data frame links every column to the same observations, row filters must preserve that alignment and column selection should retain the variables needed to interpret the result.

A logical condition can contain missing values, which may create missing rows rather than a clean exclusion unless handled explicitly. Stable code favors names and documented conditions over positions that may change when the source schema changes.

# References

[[rprimer.pdf]]
