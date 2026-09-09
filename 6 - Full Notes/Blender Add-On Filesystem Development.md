2026-09-08 09:04

Status: #baby

Tags: [[Blender Add-On Development Workflow]]

# Blender Add-On Filesystem Development

Filesystem development places an add-on directly in Blender's add-ons directory and edits it with an external text editor. The same package that appears in user preferences is therefore both the development artifact and the deployment structure.

This removes the risky conversion between scripts written in Blender's Text Editor and packages installed from disk. Single files, flat packages, and multilevel Python modules can all be valid structures. The appropriate depth depends on functional complexity and organization rather than line count alone.

# References

[[blenderpythonapi.pdf]]
