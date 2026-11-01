2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Coroutines Reactive and Testing]]

# Kotlin Integration Testing with Ktor

A Ktor integration test verifies an assembled application path rather than one isolated function. The test application can install the application's routing, middleware, serialization, and database configuration, then send an HTTP request through the resulting stack.

Ktor's `testApplication` supplies an in-process application and client. Assertions can compare the returned status and body with the public route contract. This scope catches composition failures that a unit test with mocked collaborators cannot exercise.

# References

[[masteringkotlinforjavadevelopers.epub]]
