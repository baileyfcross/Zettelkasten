2026-10-19 01:48

Status: #baby

Tags: [[Go Types Interfaces and Generics]]

# Go Rune and UTF-8 String Model

A Go `rune` is an `int32` value used for a Unicode code point, while a string is an immutable sequence of bytes conventionally containing UTF-8. Consequently, `len` reports a string's byte length, not its number of Unicode characters.

Direct indexing yields a byte and can land inside a multibyte encoding. Rune-aware iteration or Unicode utilities are needed when the application means characters rather than bytes, and conversion to a byte slice is appropriate when mutable binary content is required.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
