2026-09-08 21:16

Status: #baby

Tags: [[C Sharp Interfaces Generics and Inheritance]]

# C# Structs and Value Types

A C# struct defines a value type. Assigning or passing it normally copies its value rather than sharing the identity of one heap object, and a struct cannot inherit from another class or struct.

Structs can still define fields, methods, properties, constructors, operators, and interfaces. They are best suited to compact values whose identity is their data. Large mutable structs can create confusing copies and unnecessary movement, so class and struct are semantic as well as memory-management choices.

This copy behavior is the important contrast with a class reference: assigning a struct normally produces another value, whereas assigning a class variable normally produces another reference to the same object. Boxing is a separate conversion that places a struct value inside a managed object.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]

[[programmingincexam70-483mcsdguide.pdf]]
