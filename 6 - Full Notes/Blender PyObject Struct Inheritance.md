2026-09-14 00:20

Status: #baby

Tags: [[Blender Embedded Python Internals]]

# Blender PyObject Struct Inheritance

C has no built-in class inheritance, so CPython places a common object header at the beginning of every extension-instance structure. Blender follows this convention directly or through macros, allowing a specialized record to be treated as a base Python object.

The common header carries the object's type and reference-counting information, while later fields store extension-specific data. This prefix-layout technique supports [[Blender CPython Extension Type]] instances such as [[Blender mathutils VectorObject]] and resembles the record-prefix patterns used elsewhere in Blender's C structures.

# References

[[coreblenderdevelopment.pdf]]

