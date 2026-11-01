2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Coroutines Reactive and Testing]]

# Kotlin MockK Test Doubles

MockK creates controlled substitutes for a class, interface, or external dependency so a unit can be tested without the real collaborator. A test can prescribe return values or exceptions and verify which interactions occurred.

Annotations such as `@MockK`, `@RelaxedMockK`, and `@Spyk` distinguish full mocks, relaxed defaults, and partial mocks. Keywords such as `every` define behavior and verification operations check calls. The double is valuable when it isolates a real boundary; it should not make the test merely restate its own setup.

# References

[[masteringkotlinforjavadevelopers.epub]]
