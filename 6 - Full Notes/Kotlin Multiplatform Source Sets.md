2026-10-31 13:27

Status: #baby

Tags: [[Kotlin DSL Data and Multiplatform Applications]]

# Kotlin Multiplatform Source Sets

Kotlin Multiplatform organizes reusable logic in common source sets and keeps target-dependent code in platform source sets. Targets can include JVM, JavaScript, WebAssembly, and native platforms such as iOS, macOS, Windows, and Linux.

A shared module can feed Android code and an iOS framework while the surrounding applications retain native integration. Dependencies are attached to the source set that can use them—for example, a common test dependency or a multiplatform coroutine library—so sharing stops where a platform-specific contract begins.

# References

[[masteringkotlinforjavadevelopers.epub]]
