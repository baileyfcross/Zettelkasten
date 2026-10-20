2026-10-19 01:48

Status: #baby

Tags: [[Go Control Flow Functions and Errors]]

# Go Zero Value Initialization

Every declared Go variable receives a value even when its declaration omits an initializer. Numeric values become zero, Booleans become false, strings become empty, and pointers, maps, slices, channels, functions, and interfaces receive their appropriate nil form.

Useful zero values let many types work without a constructor, but nil-backed types differ in what operations they permit. For example, a nil slice can be appended to, whereas writing through a nil map or dereferencing a nil pointer fails.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
