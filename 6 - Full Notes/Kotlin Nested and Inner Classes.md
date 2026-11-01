2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Object-Oriented Type Design]]

# Kotlin Nested and Inner Classes

A class declared inside another Kotlin class is nested by default. It is namespaced by the outer class but does not carry an implicit reference to an outer instance, so it cannot directly read that instance's members.

Adding the `inner` modifier changes the relationship. Each inner-class instance is associated with an outer object and can access its state. The modifier therefore represents an ownership and access decision, not merely a different spelling for the same nesting structure.

# References

[[masteringkotlinforjavadevelopers.epub]]
