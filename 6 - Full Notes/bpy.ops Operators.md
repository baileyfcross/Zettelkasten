2026-09-08 09:04

Status: #baby

Tags: [[Blender Python Data and Operations]]

# bpy.ops Operators

`bpy.ops` contains operator functions that commonly mirror actions available through Blender's interface. Object operators handle whole objects and general object utilities, mesh operators work with vertices, edges, and faces, and transform operators apply translation, rotation, or scaling.

Operators are imperative and context-sensitive: they act on the current selection, active object, and mode. This makes them concise for reproducing an interface workflow, but it also means a script must establish the expected context before invoking them. Direct access through [[bpy.data Datablocks]] is preferable when a specific named value should be read or assigned without depending on selection.

# References

[[blenderpythonapi.pdf]]
