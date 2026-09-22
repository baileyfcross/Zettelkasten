2026-09-21 22:12

Status: #baby

Tags: [[Software Design Principles]]

# Liskov Substitution Principle

The Liskov substitution principle requires an implementation of a base type or interface to preserve the behavior its callers rely on. A collection of `IAnimal` objects can call `MakeNoise` on both cat and dog implementations without knowing their concrete types. Merely compiling against the same interface is not sufficient if one implementation violates the expected semantics or throws in situations the contract permits.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

