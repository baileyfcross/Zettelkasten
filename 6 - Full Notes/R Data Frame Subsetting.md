2026-10-04 22:20

Status: #baby

Tags: [[R Data Transformation and Reshaping]]

# R Data Frame Subsetting

R data frame subsetting selects rows, columns, or both by position, name, or logical condition. Because a data frame links every column to the same observations, row filters must preserve that alignment and column selection should retain the variables needed to interpret the result.

A logical condition can contain missing values, which may create missing rows rather than a clean exclusion unless handled explicitly. Stable code favors names and documented conditions over positions that may change when the source schema changes.

The student companion demonstrates two-dimensional bracket indexing, where the position before the comma selects rows and the position after it selects columns. Index vectors retain a rectangular subset, while omitting one index keeps the full corresponding dimension.

# References

[[rprimer.pdf]]

[[rstudentcompanion.pdf]]
