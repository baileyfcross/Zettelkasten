2026-09-06 20:52

Status: #baby

Tags: [[Dapper Data Access]]

# Dapper Multi-Mapping

Dapper multi-mapping divides columns from one joined row into multiple object types and uses a mapping function to assemble their relationship. It supports loading a parent and related records from one query rather than issuing a new query for every parent.

Because a join repeats parent columns for each child, the mapping code must identify existing parent objects and attach each child to the correct collection. The reduced round trips are exchanged for more deliberate assembly logic.

# References

[[aspnetcore3andreact.pdf]]
