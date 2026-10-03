2026-10-03 16:11

Status: #baby

Tags: [[Numerical PDE Methods]]

# Residual in PDE Relaxation

In a finite-difference PDE system, the residual at a mesh point is the amount left when the current trial values are substituted into that point's algebraic equation. An exact discrete solution has zero residual at every interior node.

The [[PDE Relaxation Method]] selects corrections from these residuals, often beginning with the largest one. A correction at one node also changes neighboring residuals because their stencils share that nodal value.

# References

[[numericalmethodsinengineeringandscience.pdf]]

