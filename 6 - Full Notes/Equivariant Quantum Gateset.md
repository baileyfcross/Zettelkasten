2026-10-16 23:18

Status: #baby

Tags: [[Symmetry-Equivariant Variational Quantum Learning]]

# Equivariant Quantum Gateset

An equivariant quantum gateset contains generators that commute with every unitary representing the chosen symmetry. A gate $e^{-i\theta G}$ has this property for all angles exactly when its generator $G$ commutes with the representation.

[[Quantum Gate Symmetrization by Group Twirling]] constructs such a set from a standard gateset. Under a two-qubit exchange symmetry, for example, separate $X_1$ and $X_2$ rotations collapse to one shared generator proportional to $X_1+X_2$. Adding simultaneous sign-flip symmetry can remove the analogous $Y$ and $Z$ rotations, leaving a smaller set of allowed operations.

Replacing every ansatz generator with its projected counterpart makes any composition of the resulting gates equivariant. The reduced cardinality also reduces free parameters, but [[Symmetry-Expressivity Tradeoff in Variational Quantum Circuits]] explains why fewer parameters are not automatically better.

# References

[[2022 - Exploiting symmetry in variational quantum machine learning.pdf]]

