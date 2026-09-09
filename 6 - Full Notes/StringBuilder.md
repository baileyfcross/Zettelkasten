2026-09-08 21:16

Status: #baby

Tags: [[.NET Core Data Types and Collections]]

# StringBuilder

`StringBuilder` accumulates changing text in a mutable buffer. Appending, inserting, or replacing content can reuse its storage instead of creating a new immutable string after every operation.

The builder is most useful for repeated modifications in loops or large generated output. Once construction is complete, converting it to a string produces the immutable value expected by ordinary text APIs. Simple interpolation or a few concatenations usually remain clearer for small cases.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
