2026-09-21 00:45

Status: #baby

Tags: [[COMSOL Geometry Operations]]

# COMSOL Virtual Geometry Operations

COMSOL virtual geometry operations change how the mesher interprets vertices, edges, faces, or domains without altering the underlying imported or constructed CAD geometry. Nearby entities can be merged conceptually, and small boundaries can be ignored for meshing purposes.

This approach is useful when a feature causes poor or excessively fine elements but should remain in the source representation. Because the physical geometry is untouched, the analyst must confirm that the virtual topology still supports correct boundary and domain assignments.

# References

[[geometrycreationandimport.pdf]]
