2026-09-08 09:04

Status: #baby

Tags: [[Procedural Mesh Editing with bmesh]]

# Location-Based Mesh Component Selection

Location-based selection identifies vertices, edges, or faces by testing their coordinates against a bounding region. Unlike hardcoded indices, the criterion describes where the desired geometry is, making it more resilient to topology ordering and more suitable for parameterized models.

The test must define global or local space and decide how compound components qualify. A vertex can be tested directly; an edge or face may require all, any, or a representative point of its vertices to fall within the bounds. Additive selection lets several regions be accumulated before a single mesh operation.

# References

[[blenderpythonapi.pdf]]
