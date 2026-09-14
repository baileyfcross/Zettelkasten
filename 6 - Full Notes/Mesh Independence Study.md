2026-09-14 00:55

Status: #baby

Tags: [[Thermal Model Verification and Sensitivity]]

# Mesh Independence Study

A mesh-independence study repeats the same analysis with progressively smaller elements and compares a defined output such as peak temperature, integrated heat flux, or a temperature profile. The selected mesh is adequate when further refinement changes that output insignificantly for the decision.

The comparison must preserve other solver and time-step settings so that spatial discretization is the changing factor. Local refinement near steep gradients can be more efficient than uniform refinement, but it still requires evidence from [[Thermal Mesh Refinement|successive meshes]].

# References

[[cosmolheattransfermodels.pdf]]

