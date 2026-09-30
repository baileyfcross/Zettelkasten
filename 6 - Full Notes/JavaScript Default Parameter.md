2026-09-30 00:32

Status: #baby

Tags: [[Modern JavaScript Language Features]]

# JavaScript Default Parameter

A JavaScript default parameter supplies an argument value when a caller omits that argument. The default is written in the function declaration, keeping the ordinary case near the parameter rather than requiring a separate conditional inside the body.

Defaults can be strings, numbers, objects, functions, or other values. React components in the source use the same idea for optional callback props, providing a harmless identity function so an absent callback can still be invoked without a separate existence check.

# References

[[learningreact1.pdf]]
