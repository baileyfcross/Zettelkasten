2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Collections Standard Library and File I-O]]

# Kotlin Generic Type

A Kotlin generic declaration introduces a type parameter so one class or function can operate on values of several types without discarding static type information. The actual type argument is supplied or inferred where the generic declaration is used.

Collections rely on this mechanism: a `List<String>` and a `List<Int>` share list behavior while preserving different element contracts. Constraints can narrow which types are accepted when the implementation requires operations promised by a particular upper bound.

# References

[[masteringkotlinforjavadevelopers.epub]]
