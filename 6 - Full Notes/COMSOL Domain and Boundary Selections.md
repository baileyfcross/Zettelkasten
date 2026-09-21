2026-09-14 00:55

Status: #baby

Tags: [[COMSOL Model Construction]] [[COMSOL Geometry Operations]]

# COMSOL Domain and Boundary Selections

COMSOL applies materials and volume equations to domains, surface conditions to boundaries, line features to edges, and point features to vertices. A node's geometric selection therefore determines where its mathematical statement is active.

Selections can change when geometry is rebuilt or imported, so visual inspection and named-selection strategies reduce silent misassignment. The model is incomplete until sources, interfaces, inlets, outlets, symmetry planes, and [[Thermal Boundary Condition|thermal boundaries]] are mapped to the intended entities.

# References

[[cosmolheattransfermodels.pdf]]
[[geometrycreationandimport.pdf]]
