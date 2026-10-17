2026-10-16 23:18

Status: #baby

Tags: [[Symmetry-Equivariant Variational Quantum Learning]]

# Partial Symmetry Enforcement in Variational Quantum Circuits

A variational circuit need not enforce every known symmetry exactly. One option is to build the model for a [[Subgroup]] of the full symmetry group, preserving some invariances while retaining more expressive gates. Another is to insert a limited number of explicitly symmetry-breaking operations into an otherwise equivariant ansatz.

Partial enforcement is useful when the correct symmetry sector is uncertain, because a fully commuting circuit cannot move between sectors. Carefully placed breaking gates can also repair an unfavorable loss landscape or give a shallow circuit access to states that an exact symmetry restriction would exclude.

A softer alternative leaves the ansatz unrestricted and penalizes low-symmetry states in the cost function. These choices tune the [[Symmetry-Expressivity Tradeoff in Variational Quantum Circuits]] through architecture or optimization instead of treating equivariance as all-or-nothing.

# References

[[2022 - Exploiting symmetry in variational quantum machine learning.pdf]]

