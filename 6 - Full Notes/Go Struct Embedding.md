2026-10-19 01:48

Status: #baby

Tags: [[Go Types Interfaces and Generics]]

# Go Struct Embedding

Go struct embedding includes a field by its type without an explicit field name and promotes accessible fields and methods to the containing struct. It provides composition and convenient delegation but does not create subclassing or an is-a inheritance relation.

Name collisions between embedded types must be resolved by qualification or by a field on the outer struct. Embedded values also remain independently addressable components, so code should not assume the containing type can substitute for the embedded type in every context.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
