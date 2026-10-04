2026-10-04 12:25

Status: #baby

Tags: [[.NET Core Data Types and Collections]]

# Managed and Unmanaged Code

Managed code executes under the .NET runtime. Its [[Intermediate Language]] and metadata let the runtime provide services such as type checking, exception handling, and [[Garbage Collection]] while compiling methods for the current machine.

Unmanaged code and native resources operate outside those managed lifetime guarantees. Crossing the boundary therefore requires explicit representations and ownership rules: C# unsafe code may expose memory directly, while [[Deterministic Resource Disposal]] releases native handles at a predictable time. The distinction concerns runtime governance, not whether the code is inherently good or bad.

# References

[[programmingincexam70-483mcsdguide.pdf]]
