2026-10-04 12:25

Status: #baby

Tags: [[LINQ Query Construction]]

# C# Anonymous Type

A C# anonymous type is a compiler-generated reference type created with an object-initializer expression such as `new { Name, Total }`. Its property names and types come from the initializer, and callers normally hold the result in a local `var` because the generated type has no source-level name.

Anonymous types are useful for short-lived local shapes, especially a [[LINQ Projection]] that needs only selected fields. Their inferred properties are read-only after construction. C# type inference removes the need to spell the generated type, but the compiler still assigns every property a static type.

# References

[[programmingincexam70-483mcsdguide.pdf]]
