2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Object-Oriented Type Design]]

# Kotlin Primary Constructor and Init Block

A Kotlin primary constructor is written in the class header and defines the main inputs used to create an instance. Parameters marked `val` or `var` simultaneously become properties, and default parameter values can make selected inputs optional at a call site.

Because the header has no ordinary statement body, initialization logic belongs in property initializers and `init` blocks. These blocks run as part of construction, in their declaration order, and can validate or derive state from the constructor parameters.

# References

[[masteringkotlinforjavadevelopers.epub]]
