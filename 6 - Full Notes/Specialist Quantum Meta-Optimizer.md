2026-10-17 11:48

Status: #baby

Tags: [[Meta-Learned Variational Quantum Optimization]]

# Specialist Quantum Meta-Optimizer

A specialist quantum meta-optimizer is trained on random instances drawn from one problem class and one circuit ansatz. Its objective is not to learn a generally useful optimizer over arbitrary functions, but to exploit recurring landscape structure within MaxCut QAOA, spin-glass QAOA, or Hubbard-model VQE.

Specialization turns prior solved instances into an initialization heuristic that adapts to each new instance. In the study, three separate LSTMs were trained rather than one model shared across the three tasks.

This restriction is also the source of the method's main epistemic limit. Strong performance on larger instances from the same distribution does not show that the optimizer transfers to a different Hamiltonian family, ansatz, or parameter dimension.

# References

[[2019 - Learning to learn with quantum neural networks via classical neural networks.pdf]]

