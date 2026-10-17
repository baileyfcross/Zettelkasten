2026-10-16 23:18

Status: #baby

Tags: [[Symmetry-Equivariant Variational Quantum Learning]]

# Invariant Quantum Data Re-Uploading Model

An invariant quantum data re-uploading model alternates an [[Equivariant Quantum Data Embedding]] with trainable blocks that commute with the induced symmetry representation. This preserves equivariance through every repeated encoding rather than only at the first circuit layer.

The construction also requires an initial state fixed by the representation and a measured observable unchanged under its conjugation. Under these conditions, transforming the input conjugates the final ansatz state by the group unitary, which cancels in the expectation value and leaves the prediction invariant.

The model is the symmetry-constrained counterpart of a [[Data Re-Uploading Quantum Layer]]. Its two-sided quantum structure starts from an invariant object, applies equivariant transformations, and evaluates another invariant object; [[Invariant Boundary Conditions for Quantum Learning Models]] isolates those endpoint requirements.

# References

[[2022 - Exploiting symmetry in variational quantum machine learning.pdf]]

