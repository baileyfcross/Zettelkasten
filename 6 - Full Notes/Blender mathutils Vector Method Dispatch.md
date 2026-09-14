2026-09-14 00:20

Status: #baby

Tags: [[Blender Embedded Python Internals]]

# Blender mathutils Vector Method Dispatch

When a script calls a `mathutils.Vector` method, CPython uses the type's [[Blender Python Method Table]] to invoke the registered C function. The normalization method, for example, obtains the vector data, checks callback access, calls blenlib's normalization routine, reports any write callback, and returns Python's `None`.

The same table can expose class methods, methods that mutate the original object, methods that return copies, and operations involving another value. This dispatch keeps the public Python class concise while reusing implementations from the [[Blender mathutils Extension]] and [[Blender BLI API]].

# References

[[coreblenderdevelopment.pdf]]

