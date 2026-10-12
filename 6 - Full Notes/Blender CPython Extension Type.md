2026-09-14 00:20

Status: #baby

Tags: [[Blender Embedded Python Internals]]

# Blender CPython Extension Type

A CPython extension type gives a Blender-defined C structure the behavior of a Python class. A `PyTypeObject` records its name, size, constructor, attribute accessors, method tables, allocation behavior, and other slots used by the interpreter.

The corresponding instance structure begins with the fields required by [[Blender PyObject Struct Inheritance]]. [[Blender mathutils VectorObject]] and its type record demonstrate how a constructor, [[Blender Python Method Table]], and [[Blender Python Get-Set Definition]] combine into a callable Python class.

# References

[[coreblenderdevelopment.pdf]]

