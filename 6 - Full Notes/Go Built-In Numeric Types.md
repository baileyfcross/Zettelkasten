2026-10-19 01:48

Status: #baby

Tags: [[Go Types Interfaces and Generics]]

# Go Built-In Numeric Types

Go defines signed and unsigned integers in several widths, architecture-sized `int` and `uint`, two floating-point widths, and two complex-number widths. `byte` aliases `uint8`, while `rune` aliases `int32` for Unicode code points.

Ordinary numeric variables do not widen implicitly across these types, so mixed calculations require explicit conversion. Numeric constants are untyped and represented with high precision until context assigns a compatible concrete type, making literals more flexible than variables.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
