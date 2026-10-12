2026-09-14 00:20

Status: #baby

Tags: [[Blender Embedded Python Internals]]

# Blender mathutils Vector Construction

The `mathutils.Vector` constructor allocates or accepts a float array, initializes default components, and wraps that storage in a [[Blender mathutils VectorObject]]. The default no-argument path creates a three-component zero vector using CPython allocation and a blenlib fill utility.

Specialized creation functions distinguish copied, wrapped, callback-backed, and newly allocated storage. When the extension type supplies no allocator slot, a base-math macro creates the Python object through CPython's garbage-collected allocator before returning it to the interpreter.

# References

[[coreblenderdevelopment.pdf]]

