2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Object-Oriented Type Design]]

# Kotlin Properties and Accessors

A Kotlin property is declared with `val` or `var` and is accessed through getter and, for a mutable property, setter behavior. The compiler supplies ordinary accessors automatically, so callers use property syntax without directly manipulating a field.

Custom accessors can compute a returned value, validate an assignment, or transform the stored representation. A `val` has no setter because its public contract does not allow reassignment. Accessors therefore preserve concise call syntax while giving the type control over how state is exposed or changed.

# References

[[masteringkotlinforjavadevelopers.epub]]
