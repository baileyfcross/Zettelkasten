2026-09-08 21:16

Status: #baby

Tags: [[LINQ Query Construction]]

# LINQ Join and Group

LINQ joins relate items from two sequences through matching keys. `Join` produces a flat sequence of matching pairs, while `GroupJoin` associates each outer item with a sequence of matching inner items.

Grouping organizes elements by a selected key and yields groups that can be projected or aggregated. Joins and groups make relationships explicit in the query, but the shape and cost of their translation depend on whether execution is local or delegated to a provider.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
