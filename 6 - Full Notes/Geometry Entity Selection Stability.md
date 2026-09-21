2026-09-21 00:45

Status: #baby

Tags: [[Simulation Geometry Quality]]

# Geometry Entity Selection Stability

Geometry entity selection stability is the ability of material, physics, mesh, and boundary assignments to continue identifying the intended regions after a parametric rebuild or import. Explicit numeric entity IDs are fragile because topology changes can renumber them.

Rule-based box, ball, intersection, cumulative, or named selections express the geometric criterion instead of a transient identifier. Stable selection logic makes automated sweeps safer, but every rebuilt model still needs assignment checks.

# References

[[geometrycreationandimport.pdf]]
