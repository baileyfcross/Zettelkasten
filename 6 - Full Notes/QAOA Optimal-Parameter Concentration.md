2026-10-17 11:48

Status: #baby

Tags: [[Meta-Learned Variational Quantum Optimization]]

# QAOA Optimal-Parameter Concentration

Optimal parameters for related QAOA instances can cluster in parameter space. This concentration makes the average optimum from a training set a meaningful baseline and gives a learned optimizer a structured neighborhood from which to infer instance-specific adjustments.

The paper observes the strongest concentration for MaxCut QAOA, weaker but visible concentration for Sherrington-Kirkpatrick QAOA, and the least concentration for Hubbard VQE. The ordering helps explain why a constant mean-parameter heuristic works better for the QAOA tasks than for the VQE task.

Concentration does not make a fixed initialization optimal for every instance. The LSTM's advantage is that it adapts its sequence of proposals to the measured costs and usually ends closer to the individual instance optimum than the constant training-set heuristic.

# References

[[2019 - Learning to learn with quantum neural networks via classical neural networks.pdf]]

