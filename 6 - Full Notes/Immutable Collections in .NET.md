2026-09-08 21:16

Status: #baby

Tags: [[.NET Core Data Types and Collections]]

# Immutable Collections in .NET

An immutable .NET collection cannot change its members after construction. An operation such as adding a value returns a new collection and leaves the original instance unchanged.

This behavior makes shared data easier to reason about because one consumer cannot silently modify the version another is reading. It is particularly useful for cached or multithreaded state, though producing successive versions may cost more than mutating a private ordinary collection.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
