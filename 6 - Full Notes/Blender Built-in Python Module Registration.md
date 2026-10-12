2026-09-14 00:20

Status: #baby

Tags: [[Blender Embedded Python Internals]]

# Blender Built-in Python Module Registration

Blender maintains an initialization table pairing Python module names with C initialization functions. Before the interpreter starts, the application extends CPython's built-in table with entries for modules such as `mathutils`, `bgl`, `blf`, `imbuf`, and `bmesh`.

After initialization, builds configured as a Python module may call those initializers and insert the returned modules into Python's module dictionary manually. The sequence connects the [[Blender Python Interpreter Lifecycle]] with each [[Blender CPython Extension Module]] and [[Blender mathutils Submodule Initialization]].

# References

[[coreblenderdevelopment.pdf]]

