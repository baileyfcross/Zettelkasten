2026-09-21 00:45

Status: #baby

Tags: [[COMSOL Geometry Configuration]]

# COMSOL Default Repair Tolerance

COMSOL's default repair tolerance controls when nearby geometric entities are merged or small features are removed during a geometry build. Automatic mode derives a recommended value, while relative mode lets the analyst set a threshold in relation to model size.

The setting trades unresolved gaps against unintended alteration. It should be low enough to preserve meaningful edges and high enough to form the domains required by the mesh, with measurements and build diagnostics confirming the result.

# References

[[geometrycreationandimport.pdf]]
