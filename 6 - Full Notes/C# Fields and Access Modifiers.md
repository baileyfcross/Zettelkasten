2026-09-08 21:16

Status: #baby

Tags: [[C Sharp Object-Oriented Type Design]]

# C# Fields and Access Modifiers

A field stores data inside a C# type or object. Instance fields belong to each object, while static fields belong to the type as a whole. A field can use any type, including arrays and collections.

Access modifiers control where a member is visible. Public exposes it broadly, private confines it to the declaring type, and protected or internal forms expose it to inheritance or an assembly boundary. Encapsulation chooses the narrowest visibility that still supports the intended collaboration.

The `internal` modifier restricts access to the same assembly, `protected` permits access from the declaring type and its derived types, and `protected internal` permits access through either of those routes. These scopes turn [[Encapsulation]] into a concrete boundary rather than a naming convention.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
