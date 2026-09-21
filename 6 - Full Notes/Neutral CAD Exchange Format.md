2026-09-21 00:45

Status: #baby

Tags: [[CAD and FEM Geometry Exchange]]

# Neutral CAD Exchange Format

A neutral CAD exchange format carries geometry through a published representation that multiple vendors can interpret. Formats such as STEP and IGES reduce dependence on a particular authoring application but may omit feature history, constraints, parameters, or product-specific semantics.

The receiving model should therefore be checked for changed units, missing faces, disconnected regions, and altered topology. Portability is achieved by exchanging a common subset, not by preserving every property of the native file.

# References

[[geometrycreationandimport.pdf]]
