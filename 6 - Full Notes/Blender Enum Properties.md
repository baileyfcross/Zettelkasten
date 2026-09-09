2026-09-08 09:04

Status: #baby

Tags: [[Blender Add-On Architecture]]

# Blender Enum Properties

A Blender enum property represents a choice from a predefined set and is commonly displayed as a menu. Each item associates a Python-facing identifier with a user-facing label and tooltip, plus optional icon and stable numeric information.

Separating the stored identifier from the display label lets code use compact, stable values while the interface uses readable language. In a selection add-on, enums can expose alternatives such as vertices, edges, or faces and global or local coordinates without requiring users to type exact strings.

# References

[[blenderpythonapi.pdf]]
