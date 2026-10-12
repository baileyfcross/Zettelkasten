2026-09-14 00:55

Status: #baby

Tags: [[Thermal Model Verification and Sensitivity]]

# Time-Step Independence Study

A time-step-independence study solves a transient with progressively finer temporal resolution and compares histories, peaks, and event timing. It distinguishes real dynamics from artifacts caused by stepping over rapid changes.

Output intervals do not necessarily equal internal solver steps, so the actual integration settings must be examined. The mesh, tolerances, and inputs should remain fixed while time resolution changes, complementing the separate [[Mesh and Time-Step Coupling|spatial study]].

# References

[[cosmolheattransfermodels.pdf]]

