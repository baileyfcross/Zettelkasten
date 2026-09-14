2026-09-14 00:20

Status: #baby

Tags: [[Blender Embedded Python Internals]]

# Blender mathutils Extension

`mathutils` is a built-in Blender Python extension that presents mathematical objects such as vectors, matrices, quaternions, and colors as Python classes. Its methods reuse low-level mathematical functions from the [[Blender blenlib Module]] without requiring RNA for every object.

The extension provides a compact example of the complete CPython bridge. [[Blender mathutils VectorObject]] defines instance storage, [[Blender mathutils Vector Construction]] allocates it, and [[Blender mathutils Vector Method Dispatch]] connects script-visible operations to C functions.

# References

[[coreblenderdevelopment.pdf]]

