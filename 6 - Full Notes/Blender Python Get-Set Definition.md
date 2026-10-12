2026-09-14 00:20

Status: #baby

Tags: [[Blender Embedded Python Internals]]

# Blender Python Get-Set Definition

A CPython get-set definition associates an attribute name with separate C getter and setter functions, documentation, and optional closure data. Blender uses these definitions when an attribute should expose computed or controlled access rather than a raw structure field.

For `mathutils.Vector`, the length property uses functions that read or change the vector while hiding its internal `size` member. The get-set array is attached to a [[Blender CPython Extension Type]] alongside its [[Blender Python Method Table]].

# References

[[coreblenderdevelopment.pdf]]

