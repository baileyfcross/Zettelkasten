2026-09-08 09:04

Status: #baby

Tags: [[Blender Python Scripting Environment]]

# Discovering Blender Python Operators

Blender makes operator discovery an empirical process. A developer can perform the desired interface action, inspect the resulting call in the [[Blender Command Log]], and use Python tooltips or console autocompletion to inspect the operator's parameters.

The discovered call should then be tested in the current mode and selection state because many operators depend on `bpy.context`. This method turns ordinary interface use into API exploration while also revealing which actions map cleanly to `bpy.ops` and which require direct work with Blender data.

# References

[[blenderpythonapi.pdf]]
