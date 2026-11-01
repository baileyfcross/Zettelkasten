2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Syntax Types and Control Flow]]

# Kotlin val and var Declarations

Kotlin declares a read-only local reference with `val` and a reassignable reference with `var`. A `val` receives a value once, while a `var` can receive another value later as long as the new value satisfies its type.

The compiler can infer a declaration's type from its initializer, so `val count = 3` remains statically typed even though the type name is omitted. Choosing `val` where reassignment is unnecessary makes the intended state transition narrower and more visible.

# References

[[masteringkotlinforjavadevelopers.epub]]
