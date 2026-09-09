2026-09-08 09:04

Status: #baby

Tags: [[Blender Python Data and Operations]]

# Blender Active Object in Python

The active object is the single object Blender treats as the primary target in the current context. It may be read from context and is often the object whose properties, mode, or mesh data an operator uses.

Activation does not mean the same thing as selection. Several objects can be selected while only one is active, and changing the active object can alter the result of the same context-sensitive call. A robust script establishes both the selected set and the active member before relying on an operator.

# References

[[blenderpythonapi.pdf]]
