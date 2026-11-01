2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Functions Null Safety and Delegation]]

# Kotlin let Scope Function

The Kotlin `let` scope function passes its receiver into a lambda, conventionally as `it`, and returns the lambda's result. It creates a small expression scope for transforming a value or giving it a temporary name.

Combined with a safe call, `nullableValue?.let { ... }` executes the lambda only when the receiver is non-null. This confines work that requires a present value to the branch where presence has already been established.

# References

[[masteringkotlinforjavadevelopers.epub]]
