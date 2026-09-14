2026-09-14 00:55

Status: #baby

Tags: [[COMSOL Model Construction]]

# COMSOL CAD Geometry Import

CAD import brings externally authored geometry into a COMSOL component. The imported object's spatial dimension must match the component, and repair tolerances may need adjustment so gaps, short edges, or overlapping faces do not prevent a valid domain from forming.

Imported geometry often requires simplification, partitioning, or capping before physics can be assigned. LiveLink can expose CAD parameters to the analysis tool, allowing design changes to update geometry while preserving the [[COMSOL Domain and Boundary Selections|selection logic]] needed by the model.

# References

[[cosmolheattransfermodels.pdf]]

