2026-09-08 21:16

Status: #baby

Tags: [[LINQ Query Construction]]

# LINQ Type Filtering

`OfType<T>` filters a heterogeneous sequence to elements compatible with a requested type and returns them as that type. Incompatible values, including null values when the target requires an object of the chosen type, are omitted rather than causing a cast failure.

This differs from `Cast<T>`, which attempts to cast every element and fails when an item is incompatible. Type filtering is therefore useful when a mixed sequence is expected and only one subtype is relevant to the next stage of a query.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
