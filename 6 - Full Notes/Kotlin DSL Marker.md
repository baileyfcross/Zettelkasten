2026-10-31 13:27

Status: #baby

Tags: [[Kotlin DSL Data and Multiplatform Applications]]

# Kotlin DSL Marker

A Kotlin annotation marked with `@DslMarker` identifies receiver types that participate in the same DSL. In a nested receiver lambda, it prevents an implicit reference from accidentally reaching outward to another marked receiver.

Without that restriction, a property written in an inner block may silently change an outer builder whose member happens to have the same name. The marker turns this unintended cross-scope access into a compile-time error and preserves the meaning of the nested structure.

# References

[[masteringkotlinforjavadevelopers.epub]]
