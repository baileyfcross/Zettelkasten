2026-09-14 00:55

Status: #baby

Tags: [[COMSOL Model Construction]]

# COMSOL Model Builder Tree

COMSOL organizes a model as a hierarchical tree containing global definitions, components, geometry, materials, physics, mesh, studies, and results. The tree records both the physical specification and the ordered operations used to construct and solve it.

Because settings inherit context from their node, location matters: a global parameter is available broadly, while a component definition acts locally. Reading the tree from definitions through [[COMSOL Solution Data Sets|results]] provides an audit trail of the model's assumptions and execution.

# References

[[cosmolheattransfermodels.pdf]]

