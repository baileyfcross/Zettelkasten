2026-09-08 09:04

Status: #baby

Tags: [[Blender Python Data and Operations]]

# bpy.app Module

`bpy.app` exposes information and services belonging to the running Blender application rather than to a single scene object. Of particular importance, `bpy.app.handlers` stores lists of functions that Blender calls around events such as frame changes, rendering, loading, and saving.

Application handlers make scripts reactive instead of purely sequential. A function can update data before a scene refresh or run diagnostics after a file loads. Because these hooks outlive the immediate statement that installed them, their creation, removal, and persistence need deliberate lifecycle management.

# References

[[blenderpythonapi.pdf]]
