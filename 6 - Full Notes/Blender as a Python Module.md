2026-09-08 09:04

Status: #baby

Tags: [[Blender Add-On Development Workflow]]

# Blender as a Python Module

Compiling Blender as a Python module can expose its Python namespaces to external development tools. An IDE may then inspect modules such as `bpy` for completion and support lower-level debugging workflows that are difficult when code can run only inside the Blender application.

The source treats this as an advanced, platform-dependent option rather than a guaranteed setup. Build procedures and compatibility vary across operating systems and Blender releases. Its enduring value is tighter tooling integration; its cost is a more complex development environment that must match the Blender runtime being targeted.

# References

[[blenderpythonapi.pdf]]
