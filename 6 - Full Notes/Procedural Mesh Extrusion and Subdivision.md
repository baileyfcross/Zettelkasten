2026-09-08 09:04

Status: #baby

Tags: [[Procedural Mesh Editing with bmesh]]

# Procedural Mesh Extrusion and Subdivision

Extrusion creates new connected geometry from a selected region, while subdivision inserts additional components into existing topology. In scripted modeling, these operations turn a simple primitive into a structure whose complexity is controlled by parameters rather than manual edits.

A useful sequence selects components by a reproducible characteristic, subdivides or extrudes them, and then transforms the new region. Because each operation changes the topology and may change indices, later stages should refresh BMesh access and derive their selections again instead of assuming earlier component numbers still identify the same geometry.

# References

[[blenderpythonapi.pdf]]
