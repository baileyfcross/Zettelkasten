2026-09-08 09:04

Status: #baby

Tags: [[Blender Python Data and Operations]]

# bpy.data Datablocks

`bpy.data` exposes Blender's internal datablocks, including objects, meshes, materials, textures, images, and scenes. Datablocks separate an object's identity and placement from the underlying data that defines its geometry or appearance.

Direct datablock access is declarative: assigning a named object's location overwrites that property rather than applying a relative transformation to whatever happens to be selected. It is also a stable way to retrieve data by name, inspect nested relationships, create new data containers, or remove unused ones.

# References

[[blenderpythonapi.pdf]]
