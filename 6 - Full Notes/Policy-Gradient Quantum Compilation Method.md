2026-10-12 18:17

Status: #baby

Tags: [[Policy-Gradient Variational Quantum Compilation]]

# Policy-Gradient Quantum Compilation Method

Policy-gradient variational quantum compilation learns an approximate inverse arrangement for a target unitary by optimizing a probability distribution over a parameterized circuit's angles. Each sampled angle vector defines a complete circuit rollout, and the reward is the probability that applying the target and learned reversing circuit returns a sampled input state to itself.

The paper uses a Gaussian policy and a modified REINFORCE algorithm, shifting optimization from individual gate angles to the policy's distribution parameters. This makes each update depend on rewards from several nearby angle configurations rather than a derivative evaluated only at the current point.

The method is tested only on simulated shallow circuits with known connectivity and up to 20 qubits. Its advantage appears near the edge of a barren plateau, where nonlocal sampling can encounter a slope; [[Policy-Gradient Diffusion at a Barren-Plateau Edge]] explains why it is not expected to solve optimization started deep inside a high-dimensional plateau.

# References

[[2022 - Policy Gradient Approach to Compilation of Variational Quantum Circuits.pdf]]
