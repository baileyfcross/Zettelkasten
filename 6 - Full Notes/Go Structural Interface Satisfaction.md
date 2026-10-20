2026-10-19 01:48

Status: #baby

Tags: [[Go Types Interfaces and Generics]]

# Go Structural Interface Satisfaction

A Go type satisfies an interface by having every method in the interface's method set; it does not declare an `implements` relationship. An interface can therefore be introduced after a compatible type was written, and unrelated types can satisfy the same small behavioral contract.

This structural relationship encourages consumers to accept the narrow methods they need. Satisfaction still depends on exact signatures and on value-versus-pointer method sets, so the compiler—not the author's intent—decides whether a particular value implements the interface.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
