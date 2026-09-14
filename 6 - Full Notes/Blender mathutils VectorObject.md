2026-09-14 00:20

Status: #baby

Tags: [[Blender Embedded Python Internals]]

# Blender mathutils VectorObject

`VectorObject` is the C-side instance record behind `mathutils.Vector`. It begins with base-math members that include the variable Python object header, a pointer to float data, optional callback ownership information, subtype metadata, and flags, followed by the vector's component count.

This layout uses [[Blender PyObject Struct Inheritance]] so CPython can handle the value as an ordinary object while Blender retains mathematical storage and callbacks. [[Blender mathutils Vector Construction]] determines whether the float array is owned or wrapped, and methods operate through [[Blender mathutils Vector Method Dispatch]].

# References

[[coreblenderdevelopment.pdf]]

