2026-10-14 01:16

Status: #baby

Tags: [[JavaScript Core Semantics]]

# JavaScript Hoisting

JavaScript hoisting is the common metaphor for declarations being available throughout their enclosing scope even when their textual declaration appears later. A `var` declaration belongs to its entire function scope, and a function declaration can be called before the line on which it is written.

The behavior follows from how the engine compiles declarations before execution, not from source text literally moving. Relying on an early use of a `var` binding can make code confusing because the declaration is known while its later assignment has not yet occurred; hoisted function declarations are the more customary use.

# References

[[youdontknowjs_upandgoing.pdf]]
