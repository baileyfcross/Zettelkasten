2026-09-14 00:20

Status: #baby

Tags: [[Blender Embedded Python Internals]]

# Blender Embedded Python

Blender links CPython as a library and starts an interpreter inside the application. This lets scripts invoke selected Blender functions, while Blender operators and editors can execute Python files, text blocks, or expressions through the [[Blender BPY API]].

The integration includes both embedding and extension. The [[Blender Python Interpreter Lifecycle]] controls the interpreter, while [[Blender Built-in Python Module Registration]] and [[Blender CPython Extension Type]] definitions make Blender-specific modules and classes callable from scripts.

# References

[[coreblenderdevelopment.pdf]]

