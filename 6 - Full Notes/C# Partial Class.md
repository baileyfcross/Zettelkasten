2026-09-26 22:56

Status: #baby

Tags: [[C Sharp Interfaces Generics and Inheritance]]

# C# Partial Class

A partial class divides one C# type across multiple source files. Every declaration uses the `partial` modifier and the same type name, and the compiler combines the parts into one class.

This is especially useful when generated code owns one file and handwritten extensions live in another, or when a large type must be divided for simultaneous work. The split changes source organization, not the runtime identity of the class.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

