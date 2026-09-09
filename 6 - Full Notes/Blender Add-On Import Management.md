2026-09-08 09:04

Status: #baby

Tags: [[Blender Add-On Development Workflow]]

# Blender Add-On Import Management

A multi-file Blender add-on must distinguish its first package import from later development reloads. On first load, a sibling module is imported relative to the package; on reload, the already known module is explicitly refreshed so edits become part of the running add-on.

The source uses the presence of `bpy` in local names to select these paths and imports `bpy` afterward. The exact protocol reflects its Blender and Python version, but the broader issue persists: module caches can preserve old code unless the development lifecycle deliberately refreshes dependencies.

# References

[[blenderpythonapi.pdf]]
