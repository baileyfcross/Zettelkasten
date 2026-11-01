2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Object-Oriented Type Design]]

# Kotlin Visibility Modifiers

Kotlin visibility modifiers set where a declaration may be used. `public` is the default, `private` confines access to the declaring scope, `protected` makes a class member available to that class and its subclasses, and `internal` exposes a declaration within its module.

Visibility is an architectural boundary rather than a cosmetic annotation. A narrow modifier reduces the number of callers that can depend on an implementation detail, while a wider modifier deliberately enlarges the contract that future changes must preserve.

# References

[[masteringkotlinforjavadevelopers.epub]]
