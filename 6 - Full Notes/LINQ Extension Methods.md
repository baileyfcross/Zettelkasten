2026-09-08 21:16

Status: #baby

Tags: [[LINQ Query Construction]]

# LINQ Extension Methods

Language Integrated Query is built largely from extension methods such as `Where`, `Select`, and `OrderBy`. They let query operations appear as fluent members of enumerable or queryable sequences while remaining static methods defined by the LINQ libraries.

Chaining these methods forms a pipeline in which each operation receives a sequence and produces another sequence or a final scalar value. Many operators use deferred execution, so defining the query and enumerating its results are distinct events.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
