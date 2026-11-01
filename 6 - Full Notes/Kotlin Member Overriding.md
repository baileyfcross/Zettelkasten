2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Object-Oriented Type Design]]

# Kotlin Member Overriding

A Kotlin subclass replaces eligible inherited behavior by declaring a compatible member with the `override` modifier. The modifier records that the declaration participates in an existing polymorphic contract rather than accidentally hiding a similarly named member.

The overriding implementation can call the base implementation through `super` when it needs to preserve and extend inherited behavior. Whether further subclasses may replace it remains an explicit choice, keeping the chain of specialization visible in the declarations.

# References

[[masteringkotlinforjavadevelopers.epub]]
