2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Object-Oriented Type Design]]

# Kotlin Secondary Constructor Delegation

A secondary constructor is declared with `constructor` inside a Kotlin class and supplies an alternate way to initialize an object. A class may define several such constructors when callers need distinct input shapes.

If the class has a primary constructor, each secondary constructor ultimately delegates to it, directly or through another secondary constructor, with `this(...)`. Delegation preserves one central initialization path so alternate entry points do not bypass the state established by the primary constructor and its `init` blocks.

# References

[[masteringkotlinforjavadevelopers.epub]]
