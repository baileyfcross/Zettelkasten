2026-10-19 01:48

Status: #baby

Tags: [[Go Types Interfaces and Generics]]

# Go Map Type

A Go map is a built-in associative collection from comparable keys to one value type. A lookup for an absent key returns the value type's zero value, so the two-result lookup form supplies an additional Boolean when absence must be distinguished from a stored zero.

Maps are created with `make` or a literal, grow automatically, and remove entries with `delete`. Iteration order is unspecified, which prevents callers from treating the hash table's traversal as a stable presentation or processing order.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
