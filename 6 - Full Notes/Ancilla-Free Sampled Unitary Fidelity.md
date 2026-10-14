2026-10-12 18:17

Status: #baby

Tags: [[Policy-Gradient Variational Quantum Compilation]]

# Ancilla-Free Sampled Unitary Fidelity

Ancilla-free sampled fidelity estimates a compiled unitary's performance by averaging endpoint overlaps over a polynomial-size set of orthogonal input states. It replaces the Hilbert-Schmidt test, which can estimate full gate similarity but requires a second qubit register and potentially long-range interactions.

A tomographically complete evaluation would use exponentially many inputs. Treating the sampled fidelities as bounded independent observations, the paper applies Hoeffding's inequality to show that the estimation error decreases exponentially with the number of sampled inputs. If the required error scales as an inverse power of the qubit count, a polynomial-size training set can satisfy the resulting concentration condition.

The estimate is not automatically faithful on unseen states. The ten-qubit experiments in [[Policy-Gradient Compilation Generalization]] separately test local product states and nonlocal random state vectors, showing improved test fidelity as the training set grows.

# References

[[2022 - Policy Gradient Approach to Compilation of Variational Quantum Circuits.pdf]]
