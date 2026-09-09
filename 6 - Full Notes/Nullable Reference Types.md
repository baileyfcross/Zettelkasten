2026-09-08 21:16

Status: #baby

Tags: [[C Sharp Language and Type Fundamentals]]

# Nullable Reference Types

C# 8.0 introduced an opt-in analysis mode that distinguishes reference variables intended to allow `null` from those expected to remain non-null. A `?` marks a nullable reference, while an unmarked reference produces compiler warnings when code may assign or dereference null unsafely.

This feature changes static analysis rather than the underlying runtime representation. It documents intent and moves many possible null-reference failures into compiler feedback, but callers and implementations must still check data that can genuinely be absent.

The desktop migration chapter shows the C# 8 feature as opt-in analysis that can be enabled for a file with `#nullable enable` or for a whole project in its project file. It uses constructor initialization and nullable annotations to distinguish values that must exist from those allowed to be absent.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
