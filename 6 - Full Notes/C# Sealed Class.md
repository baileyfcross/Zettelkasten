2026-09-26 22:56

Status: #baby

Tags: [[C Sharp Interfaces Generics and Inheritance]]

# C# Sealed Class

A sealed C# class cannot be used as a base class. The `sealed` modifier closes that inheritance path while leaving ordinary instantiation and member use available.

Sealing is an architectural decision: it prevents later subclasses from changing assumptions the type was not designed to expose as extension points. It contrasts with an abstract class, which exists specifically to be inherited.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]
