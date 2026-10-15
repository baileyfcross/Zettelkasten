2026-10-15 10:25

Status: #baby

Tags: [[Error-Mitigation Trainability of Variational Quantum Algorithms]]

# VD and ZNE MaxCut Optimization Limits

Finite-shot MaxCut QAOA simulations show that improved expectation-value estimators do not automatically improve an optimization run. Two- and three-copy virtual distillation fails to outperform noisy or CDR-mitigated optimization in the tested five- and eight-qubit problems, even when its total budget is allowed to reach one or two orders of magnitude more shots.

Zero-noise extrapolation is implemented by replacing CNOT gates with one, three, or five repeated CNOTs and fitting a linear extrapolation. It performs similarly to noisy optimization for $p=2$ QAOA but slightly worse for $p=4$ in the studied shot ranges. CDR remains the strongest of the compared mitigated objectives.

These results are problem- and implementation-dependent rather than universal impossibility claims. Different shot allocations, noise-scaling methods, extrapolation fits, or state-copy counts could change the comparison. They nevertheless illustrate the practical consequences of [[Virtual Distillation Resolvability Loss]] and [[Zero-Noise Extrapolation Resolvability Limit]].

# References

[[2021 - Can Error Mitigation Improve Trainability of Noisy Variational Quantum Algorithms.pdf]]
