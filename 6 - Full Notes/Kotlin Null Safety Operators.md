2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Functions Null Safety and Delegation]]

# Kotlin Null Safety Operators

Kotlin separates non-null types from nullable types marked with `?`. A safe call, `?.`, evaluates a member access only when the receiver is non-null; the Elvis operator, `?:`, supplies an alternative when the expression to its left is null.

A safe cast with `as?` returns null instead of throwing when the value has the wrong type. The non-null assertion `!!` makes the opposite tradeoff: it treats a nullable value as present and throws if that assertion is false. These operators make different absence policies explicit at the point of use.

# References

[[masteringkotlinforjavadevelopers.epub]]
