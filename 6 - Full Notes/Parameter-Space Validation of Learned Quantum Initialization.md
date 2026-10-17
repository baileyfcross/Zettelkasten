2026-10-17 11:48

Status: #baby

Tags: [[Meta-Learned Variational Quantum Optimization]]

# Parameter-Space Validation of Learned Quantum Initialization

An initializer can be evaluated by more than the cost it achieves. The paper also measures the Euclidean distance between the ten-step LSTM output and a brute-force reference optimum in circuit-parameter space.

Across fifty test instances for each task, the learned initialization is closer on average to the reference optimum than the mean training parameters used for QAOA or the adiabatic heuristic used for Hubbard VQE. This supports the interpretation that the LSTM identifies an appropriate basin rather than obtaining a favorable cost at an unrelated point.

Parameter distance is nevertheless coordinate dependent and an optimum need not be unique. The histogram evidence is best treated as corroboration of the cost curves, not as a universal measure of optimizer quality.

# References

[[2019 - Learning to learn with quantum neural networks via classical neural networks.pdf]]

