2026-09-14 00:20

Status: #baby

Tags: [[Blender Embedded Python Internals]]

# Blender mathutils Submodule Initialization

A `mathutils` submodule can expose module-level C functions through its own method array, module definition, and initialization function. The noise submodule, for example, creates its module object, installs callable functions, initializes its random seed, and returns the finished object.

Its initializer appears in the same built-in table as top-level modules, so [[Blender Built-in Python Module Registration]] does not require a separate mechanism for nested names. The pattern uses a [[Blender Python Module Definition]] rather than a [[Blender CPython Extension Type]] when no instance class is needed.

# References

[[coreblenderdevelopment.pdf]]

