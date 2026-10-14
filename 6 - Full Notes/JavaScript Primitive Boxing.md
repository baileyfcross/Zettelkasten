2026-10-14 01:16

Status: #baby

Tags: [[JavaScript Core Semantics]]

# JavaScript Primitive Boxing

JavaScript primitive strings, numbers, and booleans can expose properties and methods even though they are not ordinary objects. When code accesses a method such as `toUpperCase()` on a string, the language temporarily boxes the primitive with its corresponding object wrapper.

The wrapper supplies behavior through its prototype and remains mostly invisible to the program. The source recommends using primitive values directly in normal code and letting JavaScript perform this automatic boxing rather than constructing `String`, `Number`, or `Boolean` wrapper objects explicitly.

# References

[[youdontknowjs_upandgoing.pdf]]
