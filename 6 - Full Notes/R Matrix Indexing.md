2026-10-04 22:56

Status: #baby

Tags: [[R Matrix Systems and Scientific Models]]

# R Matrix Indexing

R matrix indexing selects an entry, row, column, or submatrix with separate row and column indexes inside square brackets. Index vectors can reorder or repeat positions, while leaving one side blank retains the entire corresponding dimension.

Preserving a two-dimensional result matters when the selection will participate in later matrix algebra. A single selected row or column may otherwise simplify to a vector and change how subsequent operations interpret its shape.

# References

[[rstudentcompanion.pdf]]
