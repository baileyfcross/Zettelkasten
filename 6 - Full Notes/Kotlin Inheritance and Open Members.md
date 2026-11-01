2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Object-Oriented Type Design]]

# Kotlin Inheritance and Open Members

Kotlin classes and members are closed to ordinary inheritance by default. A superclass must be marked `open`, and a member must also be `open` before a subclass can replace its implementation.

A derived class names its superclass after a colon and supplies any constructor arguments required by the base type. This explicit opt-in makes extension part of the original type's design contract instead of assuming that every implementation detail is safe for subclasses to specialize.

# References

[[masteringkotlinforjavadevelopers.epub]]
