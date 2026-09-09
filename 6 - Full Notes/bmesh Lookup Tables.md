2026-09-08 09:04

Status: #baby

Tags: [[Procedural Mesh Editing with bmesh]]

# bmesh Lookup Tables

BMesh vertex, edge, and face sequences require lookup tables before reliable integer indexing. Calling `ensure_lookup_table()` synchronizes the indexable view and helps avoid errors caused by references to components that have been added, removed, or reordered.

Procedural topology changes make old indexing assumptions especially fragile. Rebuilding lookup tables liberally is a small cost compared with using a stale reference, but it does not make an index semantically stable across Blender versions or earlier mesh transformations. [[Blender Mesh Index Compatibility]] therefore remains a separate design concern.

# References

[[blenderpythonapi.pdf]]
