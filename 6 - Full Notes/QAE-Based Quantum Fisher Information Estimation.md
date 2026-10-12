2026-10-12 01:15

Status: #baby

Tags: [[Quantum Autoencoding and State Compression]]

# QAE-Based Quantum Fisher Information Estimation

QAE-based quantum Fisher information estimation turns low-rank fidelity estimates into an objective for quantum sensing. A variationally prepared probe interacts with a parameter-dependent process at two nearby parameter values. [[QAE-Based Low-Rank Fidelity Estimation]] estimates the fidelity between the resulting states, and a finite-difference relation converts that fidelity into an estimate of quantum Fisher information.

The probe circuit can then be optimized to increase the estimate, seeking a state with greater sensitivity to the unknown parameter. In the paper's four-qubit magnetic-field simulation, the method approached the exact optimum, showing how quantum autoencoding can serve a larger variational protocol rather than only a standalone compression task.

Accuracy depends jointly on the separation between the two parameter values and on compression quality. This interaction is captured by the [[Quantum Fisher Information Shift Tradeoff]] and prevents an arbitrarily small finite-difference step from automatically producing the best practical estimate.

# References

[[2021 - On exploring practical potentials of quantum auto-encoder with advantages.pdf]]
