2026-09-08 09:04

Status: #baby

Tags: [[Procedural Mesh Editing with bmesh]]

# Blender Mesh Index Compatibility

Hardcoded vertex, edge, and face indices may reproduce a result within one controlled Blender version and mesh history, but they are not dependable semantic identifiers. Version changes and topology operations can reorder components even when the visible model remains similar.

Shared or long-lived scripts should select geometry by characteristics such as position, bounds, connectivity, or orientation. Index-based access remains practical when the input and execution history are strictly controlled, but that constraint should be explicit. Lookup-table refreshes prevent stale access errors; they do not solve cross-version meaning.

# References

[[blenderpythonapi.pdf]]
