2026-09-08 09:04

Status: #baby

Tags: [[Blender Python Data and Operations]] · [[Blender RNA Data Architecture]]

# Blender bpy Module

The `bpy` module is the central Python interface to Blender. Its namespaces separate actions from state: `bpy.ops` invokes operators, `bpy.context` describes the current working context, `bpy.data` exposes persistent datablocks, and `bpy.app` provides application-level information and event handlers.

This division suggests two styles of automation. Operator calls resemble actions a user performs and often depend on mode or selection, while direct datablock access names and changes data explicitly. Effective scripts combine both while remaining clear about which state each operation relies on.

Internally, `bpy.data` is created through the [[Blender Python RNA Bridge]]: Blender wraps its [[Blender Main Database]] in a [[Blender PointerRNA]] and then in a CPython extension object. Custom attribute functions route Python reads and writes through the RNA Data API instead of exposing raw DNA structures.

# References

[[blenderpythonapi.pdf]]

[[coreblenderdevelopment.pdf]]
