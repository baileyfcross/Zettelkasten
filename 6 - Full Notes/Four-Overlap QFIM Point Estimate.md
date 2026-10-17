2026-10-17 14:27

Status: #baby

Tags: [[Stochastic Quantum Natural-Gradient Optimization]]

# Four-Overlap QFIM Point Estimate

A QN-SPSA metric sample uses two independent random directions, $\Delta_1$ and $\Delta_2$, and four fidelities involving the current state and nearby parameter points. The second-order difference compares overlaps at $\theta\pm\epsilon\Delta_1$ with and without the additional displacement $\epsilon\Delta_2$.

Multiplying that difference by the symmetrized directional outer product gives a stochastic estimate of the [[Fidelity-Hessian Representation of the QFIM]]. The number of overlap measurements per point sample is four and does not grow with the number of circuit parameters.

Each point sample has rank at most two. It therefore cannot by itself represent a full high-dimensional metric; useful curvature emerges through [[Smoothed Stochastic QFIM Estimate|averaging across iterations or repeated samples]].

# References

[[2021 - Simultaneous Perturbation Stochastic Approximation of the Quantum Fisher Information.pdf]]

