2026-09-26 22:56

Status: #baby

Tags: [[C Sharp Interfaces Generics and Inheritance]]

# Generic Type Constraint

A generic type constraint limits which type arguments may replace a type parameter. A `where` clause can require a particular base class or interface, or distinguish reference types with `class` from value types with `struct`.

Constraints let generic code safely use members promised by the constraint instead of treating the parameter as an unconstrained unknown. Multiple compatible constraints can express a more precise contract for a [[Generic Type]] or [[Generic Method]].

Go expresses constraints as interfaces that may require methods or list a union of permitted type terms. `any` accepts every type, `comparable` admits equality-compatible values, and a tilde term includes named types whose underlying type matches the stated term.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]

