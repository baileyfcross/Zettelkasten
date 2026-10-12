2026-09-21 22:12

Status: #baby

Tags: [[Software Design Principles]]

# Liskov Substitution Principle

The Liskov substitution principle requires an implementation of a base type or interface to preserve the behavior its callers rely on. A collection of `IAnimal` objects can call `MakeNoise` on both cat and dog implementations without knowing their concrete types. Merely compiling against the same interface is not sufficient if one implementation violates the expected semantics or throws in situations the contract permits.

The source frames substitution as the requirement that a derived type remain usable through the base type's contract. If a subtype rejects valid base inputs or violates expected behavior, inheritance has created coupling rather than a safe specialization.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

[[hands-ondesignpatternswithcandnetcore.pdf]]
