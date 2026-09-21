2026-09-21 00:45

Status: #baby

Tags: [[CAD and FEM Geometry Exchange]]

# Geometry Import Repair Tolerance

Geometry import repair tolerance defines the distance below which the receiving application may treat nearby vertices or edges as coincident. It can close small gaps and eliminate features that would otherwise prevent a connected domain.

A tolerance set too low leaves defects unrepaired; one set too high merges intended detail or changes boundaries. The value must be chosen relative to model scale and verified against known dimensions and required features after import.

# References

[[geometrycreationandimport.pdf]]
