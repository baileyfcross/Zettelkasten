2026-09-08 09:04

Status: #baby

Tags: [[Blender Add-On Development Workflow]]

# Reloading Blender Add-Ons

In Blender 2.78c, reloading active add-ons unregisters their current in-memory classes, recompiles changed Python files, and registers the new code. The source presents the F8 command as a fast development loop for packages being edited directly in Blender's filesystem.

Reloading all active add-ons also tests interactions among dependencies, but it increases the importance of complete cleanup. A stale class, property, or handler can make the next registration misleading. Console messages around unregistration and registration reveal which code version Blender actually loaded.

# References

[[blenderpythonapi.pdf]]
