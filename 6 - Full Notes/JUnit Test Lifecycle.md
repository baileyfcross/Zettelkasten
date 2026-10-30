2026-10-30 15:57

Status: #baby

Tags: [[Java Diagnostics Testing and Documentation]]

# JUnit Test Lifecycle

JUnit 5 discovers methods marked as tests and supplies lifecycle annotations for setup and cleanup before or after each test or once per test class. A test class organizes related cases, while display names, disabling, repetition, and parameterization describe how individual cases are executed.

Per-test setup should establish an independent known state so execution order does not affect results. Shared class-level fixtures can reduce cost but increase coupling, requiring explicit lifecycle choices and cleanup when they contain mutable or external resources.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
