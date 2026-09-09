2026-09-08 09:04

Status: #baby

Tags: [[Procedural Mesh Editing with bmesh]]

# Blender Edit Mode Automation

Object Mode operations treat a mesh object as a whole, while Edit Mode exposes its vertices, edges, and faces. Granular procedural modeling therefore requires a script to enter Edit Mode, establish a component selection, perform mesh operations, and return to a safe mode when object-level work resumes.

Mode is part of Blender's context, not merely a visual preference. An operator that succeeds in Object Mode may be invalid in Edit Mode, and `bmesh.from_edit_mesh` expects editable mesh data. Wrapper functions that set mode and clear stale selections make later modeling steps more predictable.

# References

[[blenderpythonapi.pdf]]
