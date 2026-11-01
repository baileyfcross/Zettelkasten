2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Syntax Types and Control Flow]]

# Kotlin Type Checks and Smart Casts

The `is` operator checks whether a value has a specified runtime type, and `!is` expresses the negative test. After a successful check, Kotlin can smart-cast the value so members of the more specific type can be used without a repeated explicit cast.

A smart cast depends on the compiler being able to prove that the reference cannot change between the check and its use. The feature therefore joins control-flow analysis to the type system: the branch condition supplies evidence that narrows the usable type inside that branch.

# References

[[masteringkotlinforjavadevelopers.epub]]
