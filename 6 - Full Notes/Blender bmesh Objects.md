2026-09-08 09:04

Status: #baby

Tags: [[Procedural Mesh Editing with bmesh]]

# Blender bmesh Objects

The `bmesh` module presents editable mesh topology through collections of vertices, edges, and faces. In Edit Mode, `bmesh.from_edit_mesh` obtains a BMesh associated with the active object's mesh data, allowing component-level inspection and modification.

BMesh instances should be treated as temporary working views rather than durable application data. They can become invalid after Blender updates or garbage collection, so scripts should acquire them near the operation that needs them and rebuild lookup tables when topology may have changed.

# References

[[blenderpythonapi.pdf]]
