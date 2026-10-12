2026-09-14 00:55

Status: #baby

Tags: [[Finite Element Thermal Modeling]]

# Finite Element Thermal Discretization

The finite element method replaces a continuous thermal domain with a collection of small elements joined at nodes. Within each element, temperature is approximated from nodal values, allowing the governing heat equation to become a finite system of algebraic equations.

Discretization makes irregular geometry and nonuniform properties tractable, but it introduces approximation error. Element type, size, and distribution must resolve important gradients, and a [[Mesh Independence Study|refinement study]] must show that the chosen mesh supports the reported quantity.

# References

[[cosmolheattransfermodels.pdf]]

