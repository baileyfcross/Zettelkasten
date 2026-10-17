2026-10-16 23:18

Status: #baby

Tags: [[Symmetry-Equivariant Variational Quantum Learning]]

# Symmetry-Invariant Quantum Model Generalization

A symmetry-invariant quantum model can accept lower training accuracy than an unconstrained counterpart yet achieve higher accuracy on unseen data. The restriction removes functions that assign different labels to symmetry-related inputs, reducing variance in a way aligned with the task rather than through an arbitrary capacity penalty.

In the paper's nine-qubit tic-tac-toe experiments, dihedral-invariant circuits generally matched or trailed non-invariant training performance but produced a smaller generalization gap and higher test accuracy across architecture sizes and randomized layer layouts. A rotationally invariant autonomous-driving toy classifier showed the same overall pattern.

These are small noiseless simulations, not a scaling or quantum-advantage result. They nevertheless support the mechanism proposed by [[Symmetry-Invariant Variational Quantum Learning]]: a correct structural bias can improve test behavior even while reducing expressivity.

# References

[[2022 - Exploiting symmetry in variational quantum machine learning.pdf]]

