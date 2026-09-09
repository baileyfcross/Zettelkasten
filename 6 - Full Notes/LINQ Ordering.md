2026-09-08 21:16

Status: #baby

Tags: [[LINQ Query Construction]]

# LINQ Ordering

LINQ orders a sequence with `OrderBy` or `OrderByDescending` and adds subordinate keys with `ThenBy` or `ThenByDescending`. Each key selector extracts the value used at that level of comparison.

Calling a new `OrderBy` starts a new primary ordering, whereas `ThenBy` preserves the existing priority. Stable, explicit ordering is essential whenever consumers depend on deterministic presentation, paging, or selection of first and last elements.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
