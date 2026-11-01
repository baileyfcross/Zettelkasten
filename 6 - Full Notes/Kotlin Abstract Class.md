2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Object-Oriented Type Design]]

# Kotlin Abstract Class

An abstract Kotlin class cannot be instantiated directly. It can hold implemented state and behavior while declaring abstract members whose implementation is deferred to a concrete subclass.

Abstract members need no `open` modifier because replacement is inherent in their contract. The form is useful when related types share implementation as well as an incomplete protocol, but construction should be reserved for a descendant that supplies all required behavior.

# References

[[masteringkotlinforjavadevelopers.epub]]
