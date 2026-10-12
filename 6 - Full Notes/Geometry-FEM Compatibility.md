2026-09-21 00:45

Status: #baby

Tags: [[CAD and FEM Geometry Exchange]]

# Geometry-FEM Compatibility

Geometry-FEM compatibility means that imported vertices, edges, faces, and volumes satisfy the receiving solver's requirements for connected domains, entity tolerances, dimension, and meshing. Correct CAD dimensions alone do not establish this compatibility.

Tiny gaps, overlapping entities, sliver faces, and incorrect junctions may be invisible in the authoring tool yet prevent continuity or create poor elements. The FEM specialist must inspect the imported topology in the host environment.

# References

[[geometrycreationandimport.pdf]]
