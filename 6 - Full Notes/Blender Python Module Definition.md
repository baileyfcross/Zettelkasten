2026-09-14 00:20

Status: #baby

Tags: [[Blender Embedded Python Internals]]

# Blender Python Module Definition

A CPython module definition describes a C-created module through its name, documentation, state size, function table, and optional reload, traversal, clear, and free callbacks. Blender passes this record to the module-creation API when initializing an extension.

The definition packages module-level functions using the same style as a [[Blender Python Method Table]]. It is central to [[Blender CPython Extension Module]] construction and lets [[Blender mathutils Submodule Initialization]] expose functions without requiring a class instance.

# References

[[coreblenderdevelopment.pdf]]

