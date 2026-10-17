2026-10-16 23:18

Status: #baby

Tags: [[Symmetry-Equivariant Variational Quantum Learning]]

# Symmetry-Invariant Variational Quantum Learning

A variational quantum learning model is symmetry-invariant when applying an allowed transformation to its classical input leaves its prediction unchanged. If a group element $s$ acts on data as $V_s$, the required relation is $y(V_s[x])=y(x)$.

This requirement is a task-specific inductive bias. Inputs on the same symmetry orbit are forced to share a prediction, reducing the set of functions the model can express and preventing it from spending parameters on distinctions that the label is known to ignore. [[Symmetry-Invariant Quantum Model Generalization]] describes the empirical benefit, while [[Equivariant Quantum Data Embedding]] begins the circuit construction.

The word invariant applies to the final prediction, not necessarily to every intermediate state. Intermediate circuit operations can instead be equivariant: they transform compatibly with the symmetry so that invariance can be imposed at readout.

# References

[[2022 - Exploiting symmetry in variational quantum machine learning.pdf]]

