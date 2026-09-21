2026-09-14 00:55

Status: #baby

Tags: [[COMSOL Model Construction]] [[COMSOL Geometry Configuration]]

# COMSOL Component and Study Structure

A COMSOL component groups a geometry with its local definitions, materials, physics interfaces, and mesh. A model can contain multiple components when different geometries or dimensional representations must coexist.

Studies specify which physics are solved and whether the solution is stationary, time dependent, parametric, or sequenced through multiple steps. Separating component structure from study structure lets the same physical model support several analyses without duplicating its entire [[COMSOL Model Builder Tree|model tree]].

# References

[[cosmolheattransfermodels.pdf]]
[[geometrycreationandimport.pdf]]
