2026-09-14 00:20

Status: #baby

Tags: [[Blender Embedded Python Internals]]

# Blender CPython Extension Module

A Blender CPython extension module is a module object created by C and exposed inside the embedded interpreter. CPython functions create the module, add class or function objects, and register its initialization routine before Python starts.

The module's description and callable table are held by a [[Blender Python Module Definition]]. Classes added to it use [[Blender CPython Extension Type]] records, while module-level subpackages such as noise follow the [[Blender mathutils Submodule Initialization]] pattern.

# References

[[coreblenderdevelopment.pdf]]

