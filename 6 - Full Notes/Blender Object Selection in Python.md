2026-09-08 09:04

Status: #baby

Tags: [[Blender Python Data and Operations]]

# Blender Object Selection in Python

Selection is a set-valued state: no objects, one object, or many objects may be selected simultaneously. Blender operators commonly apply to that set, so scripted selection determines the scope of subsequent transforms, deletions, and other actions.

Selection is distinct from [[Blender Active Object in Python]]. One selected object can be designated active for context-dependent operations, while another named object can be accessed through `bpy.data` without selecting it at all. Scripts become more predictable when they explicitly establish each of these states instead of treating them as interchangeable.

# References

[[blenderpythonapi.pdf]]
