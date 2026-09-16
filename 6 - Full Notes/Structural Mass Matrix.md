2026-09-16 08:45

Status: #baby

Tags: [[Finite Element Dynamics]]

# Structural Mass Matrix

A structural mass matrix distributes element mass among nodal degrees of freedom so inertia can enter the finite element equations. Its coefficients depend on density, geometry, element length, and interpolation functions.

Element mass matrices are assembled using the same local-to-global mapping as stiffness matrices. In free vibration, the global mass matrix is multiplied by squared frequency in the generalized eigenvalue problem.

# References

[[finiteelementanalysis_aprimer.pdf]]
