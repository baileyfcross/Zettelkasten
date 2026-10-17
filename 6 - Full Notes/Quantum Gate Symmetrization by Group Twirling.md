2026-10-16 23:18

Status: #baby

Tags: [[Symmetry-Equivariant Variational Quantum Learning]]

# Quantum Gate Symmetrization by Group Twirling

Group twirling converts an operator $G$ into one that commutes with a unitary symmetry representation. For a finite group it averages all conjugates,

$$\mathcal{T}_U[G]=\frac{1}{|S|}\sum_{s\in S}U_sGU_s^\dagger,$$

and for a compact Lie group the sum becomes an integral over its uniform Haar measure.

The map is a projector onto the commutant of the representation. Exponentiating the projected generator therefore produces a parameterized gate whose order can be exchanged with every symmetry operation. Applying the projection to each generator is the basic construction behind an [[Equivariant Quantum Gateset]].

Twirling can identify different generators or map them to zero. It should therefore be understood as a structural projection, not as an innocuous averaging that preserves the original ansatz's expressivity.

# References

[[2022 - Exploiting symmetry in variational quantum machine learning.pdf]]

