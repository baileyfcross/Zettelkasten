2026-10-16 22:51

Status: #baby

Tags: [[Quantum Generative Architecture Performance]]

# QCBM Direct Distribution Training

A quantum circuit Born machine trains a parameterized state so its measurement probabilities approximate the normalized histogram of a target dataset. The benchmark minimizes forward Kullback-Leibler divergence between the target histogram $Q$ and the circuit distribution $P(\theta)$ with a classical optimizer and no discriminator.

Removing adversarial dynamics makes QCBM training a diagnostic for the chosen circuit ansatz. Poor convergence can be attributed more directly to representation and optimization rather than to an imbalance between generator and discriminator learning rates.

The study uses gradient-free CMA-ES and state-vector simulation for its direct objective. That setup requires access to probabilities or sufficiently complete sampling of the grid; it becomes costly as circuit width grows and does not by itself show how a hardware-trained QCBM would scale.

# References

[[2023 - A performance characterization of quantum generative models.pdf]]

