2026-10-12 18:17

Status: #baby

Tags: [[Policy-Gradient Variational Quantum Compilation]]

# Endpoint-Fidelity Quantum Compilation Reward

The compilation reward is the squared overlap between an initial state and the state obtained after applying the target unitary followed by the learned reversing circuit. Averaging this endpoint fidelity across sampled inputs measures how closely the combined operation returns those inputs to their starting states.

Because the reward is measured only after the full circuit, the algorithm does not require intermediate projective measurements that would collapse the evolving state. A complete rollout samples every variational angle at once, executes the circuit, and supplies one terminal [[Reinforcement Learning Reward Function]] to the policy update.

Endpoint fidelity avoids the extra register and long-range interactions required by a Hilbert-Schmidt test, but it observes only the selected inputs. [[Ancilla-Free Sampled Unitary Fidelity]] therefore makes training cheaper at the cost of an explicit generalization question.

# References

[[2022 - Policy Gradient Approach to Compilation of Variational Quantum Circuits.pdf]]
