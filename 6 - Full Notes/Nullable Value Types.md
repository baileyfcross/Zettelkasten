2026-09-08 21:16

Status: #baby

Tags: [[C Sharp Language and Type Fundamentals]]

# Nullable Value Types

A value type normally always contains a value, but appending `?` creates a nullable form that can also represent `null`. This is useful when a number, date, or other value is absent in an external source such as a database.

A nullable value reports whether it has a value and exposes that value only when present. Code should test or safely unwrap it before use. The null-coalescing operator can provide a fallback when absence has a sensible default.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
