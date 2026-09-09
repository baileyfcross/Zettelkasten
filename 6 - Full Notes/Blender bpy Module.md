2026-09-08 09:04

Status: #baby

Tags: [[Blender Python Data and Operations]]

# Blender bpy Module

The `bpy` module is the central Python interface to Blender. Its namespaces separate actions from state: `bpy.ops` invokes operators, `bpy.context` describes the current working context, `bpy.data` exposes persistent datablocks, and `bpy.app` provides application-level information and event handlers.

This division suggests two styles of automation. Operator calls resemble actions a user performs and often depend on mode or selection, while direct datablock access names and changes data explicitly. Effective scripts combine both while remaining clear about which state each operation relies on.

# References

[[blenderpythonapi.pdf]]
