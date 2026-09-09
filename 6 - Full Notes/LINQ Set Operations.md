2026-09-08 21:16

Status: #baby

Tags: [[LINQ Query Construction]]

# LINQ Set Operations

LINQ set operators compare sequences according to element equality. `Distinct` removes duplicates, `Union` combines unique values, `Intersect` keeps values found in both inputs, and `Except` keeps values from the first input that are absent from the second.

Correct results depend on the equality semantics of the element type or an explicitly supplied comparer. These operations describe mathematical membership, so they should not be used when duplicate counts or original ordering carry essential meaning.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
