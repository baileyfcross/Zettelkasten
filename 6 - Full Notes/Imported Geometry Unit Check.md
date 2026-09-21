2026-09-21 00:45

Status: #baby

Tags: [[CAD and FEM Geometry Exchange]]

# Imported Geometry Unit Check

An imported geometry unit check compares known lengths, areas, or volumes in the receiving application with authoritative source dimensions. It detects scale factors introduced when CAD and simulation tools interpret the same coordinates under different unit systems.

The check should be a required post-import checkpoint even for simple geometry. A scale error may not produce a solver warning, yet it changes material volume, mesh size, heat-transfer area, stiffness, and every dimensional result derived from the model.

# References

[[geometrycreationandimport.pdf]]
