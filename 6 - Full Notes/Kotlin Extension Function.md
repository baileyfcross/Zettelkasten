2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Functions Null Safety and Delegation]]

# Kotlin Extension Function

A Kotlin extension function declares a receiver type before the function name and can then be called with member-like syntax on values of that type. Inside the function, `this` refers to the receiver.

The extension does not modify the receiver's class or gain privileged access to its private members. It is resolved from the statically available declarations, making it a way to organize related operations and fluent APIs rather than a mechanism for changing the class's actual inheritance or member table.

# References

[[masteringkotlinforjavadevelopers.epub]]
