2026-09-26 22:56

Status: #baby

Tags: [[C Sharp Object-Oriented Type Design]]

# Abstraction

Abstraction presents the behavior relevant to a caller while hiding implementation details that do not belong in that caller's decision. A C# interface or abstract base class can express the stable contract, leaving concrete types to supply different implementations.

This separation makes code easier to change when clients depend on what an object promises rather than how it currently performs the work. It also supports polymorphism by giving different objects a common surface.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]
