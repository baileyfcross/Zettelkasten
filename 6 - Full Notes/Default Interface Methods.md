2026-09-08 21:16

Status: #baby

Tags: [[C Sharp Interfaces Generics and Inheritance]]

# Default Interface Methods

C# 8.0 allows an interface member to provide a default implementation. A new member can therefore be added to an interface without immediately forcing every existing implementing type to supply its own body.

The feature supports contract evolution, but it does not turn an interface into an ordinary stateful base class. Implementations can override the default, and callers should still treat the interface primarily as the declaration of a shared capability.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
