2026-09-08 09:04

Status: #baby

Tags: [[Procedural Mesh Editing with bmesh]]

# bmesh Vertex Edge and Face Selection

A BMesh exposes vertex, edge, and face collections whose members carry selection state. Scripts can set each component's selection Boolean directly, then use ordinary Edit Mode operators to transform or modify the selected region.

Blender's current component-selection mode affects how this state is displayed and how connected elements respond. A face implies boundary edges and vertices geometrically, but a script should still select the kind of component its next operation expects. Clearing previous selections prevents an intended local edit from reaching unrelated topology.

# References

[[blenderpythonapi.pdf]]
