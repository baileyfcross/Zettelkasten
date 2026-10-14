2026-10-14 01:16

Status: #baby

Tags: [[JavaScript Core Semantics]]

# JavaScript Module Pattern

The JavaScript module pattern uses a function scope to hide implementation variables and functions, then returns an object containing the public operations that outside code may call. Those operations retain access to the private state through [[JavaScript Closure|closure]].

Each ordinary call to the module-producing function creates a new scope and therefore a separate module instance. This pattern does not require construction with `new`; its boundary comes from lexical scope and the deliberately returned public API rather than from a class instance.

# References

[[youdontknowjs_upandgoing.pdf]]
