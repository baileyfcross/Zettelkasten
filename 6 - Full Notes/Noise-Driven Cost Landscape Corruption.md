2026-10-15 10:25

Status: #baby

Tags: [[Error-Mitigation Trainability of Variational Quantum Algorithms]]

# Noise-Driven Cost Landscape Corruption

Noise can damage a variational objective without uniformly flattening it. It may move a minimum, change the ordering of candidate parameters, break an ideal degeneracy, create spurious local structure, or distort different regions by different amounts. These effects are cost-landscape corruption rather than pure cost concentration.

The distinction matters because an error-mitigation method can be neutral or harmful for concentration while still repairing enough corruption to improve optimization. [[Clifford Data Regression Trainability Window]] exploits this possibility: an affine correction does not improve pairwise relative resolvability when applied identically, but it can make the observed landscape better aligned with the ideal one.

Conversely, restoring expectation values on average does not prove that the optimizer will find better parameters. Trainability depends jointly on landscape fidelity, cost separation, statistical variance, and the finite shot allocation used during the search.

# References

[[2021 - Can Error Mitigation Improve Trainability of Noisy Variational Quantum Algorithms.pdf]]
