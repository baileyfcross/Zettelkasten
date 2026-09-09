2026-09-08 09:04

Status: #baby

Tags: [[Blender Python Data and Operations]]

# bpy.context State

`bpy.context` exposes the state in which a Blender operation is evaluated. It can identify the scene, mode, selected objects, active object, and data associated with the current interface area. Operator behavior often changes or becomes unavailable when this state does not meet its requirements.

Context is a convenient path to what the user is currently working with, but it is not a permanent identity for that data. When a script needs a particular object regardless of interface focus, [[Blender Object Lookup by Name]] through `bpy.data` makes that dependency explicit.

# References

[[blenderpythonapi.pdf]]
