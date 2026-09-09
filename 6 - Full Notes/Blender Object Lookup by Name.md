2026-09-08 09:04

Status: #baby

Tags: [[Blender Python Data and Operations]]

# Blender Object Lookup by Name

A Blender object can be specified directly by indexing the objects collection in `bpy.data` with its name. This retrieves a particular datablock independently of which object is selected or active in the interface.

Named lookup is useful for declarative changes and relationships that should not depend on current user state. Its corresponding risk is name instability: renaming or deleting the object breaks the assumption. Scripts that use names should therefore control naming at creation time or validate that the expected datablock exists.

# References

[[blenderpythonapi.pdf]]
