2026-10-31 13:27

Status: #baby

Tags: [[Kotlin DSL Data and Multiplatform Applications]]

# Kotlin Type-Safe Builder

A Kotlin type-safe builder collects configuration through a structured lambda and then constructs the target object with a `build` operation. Mutable builder properties can gather inputs even when the resulting object's properties are read-only.

Receiver lambdas allow nested blocks to configure the current builder without repeatedly naming it. Collections can accumulate repeated nested values, such as several addresses, before one immutable result is created. The compiler still checks the available receiver members and value types.

# References

[[masteringkotlinforjavadevelopers.epub]]
