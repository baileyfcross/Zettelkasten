2026-10-04 12:25

Status: #baby

Tags: [[C Sharp Language and Type Fundamentals]]

# C# Unsafe Code

C# unsafe code permits pointer declarations, pointer arithmetic, and direct access to memory locations that ordinary managed references do not expose. An unsafe context is marked with the `unsafe` keyword, and the project must explicitly allow unsafe compilation.

The feature is intended for low-level work such as native interoperability or specialized memory access. Because pointer operations bypass some runtime checks, the programmer assumes responsibilities normally handled by the managed type system and [[Garbage Collection]]. Keeping the unsafe region small makes its boundary with [[Managed and Unmanaged Code]] easier to audit.

# References

[[programmingincexam70-483mcsdguide.pdf]]
