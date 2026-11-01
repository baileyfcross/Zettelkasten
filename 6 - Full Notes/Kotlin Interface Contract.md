2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Object-Oriented Type Design]]

# Kotlin Interface Contract

A Kotlin interface describes functions and properties that an implementing type promises to provide. It may leave members abstract or include default method behavior, allowing a contract to share an implementation without becoming the object's state-bearing superclass.

Interfaces can inherit from other interfaces, and a class can implement more than one. This composes capabilities across otherwise unrelated types. When inherited defaults conflict, the implementing class must resolve the ambiguity instead of silently receiving an arbitrary behavior.

# References

[[masteringkotlinforjavadevelopers.epub]]
