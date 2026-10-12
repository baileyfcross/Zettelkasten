2026-10-12 18:17

Status: #baby

Tags: [[Policy-Gradient Variational Quantum Compilation]]

# REINFORCE Quantum Circuit Parameter Update

The circuit update uses the REINFORCE score-function identity to express the gradient of expected fidelity as an expectation of reward multiplied by the gradient of the policy log likelihood. A small batch of sampled circuit rollouts can therefore estimate a classical gradient for the Gaussian mean without differentiating the quantum circuit at a single angle configuration.

The experiments use five to ten episodes per policy update. RMSprop rescales each policy-parameter step using a moving average of gradient variance, and the mean reward of the batch acts as a baseline so above-average rollouts receive positive advantage while common reward fluctuations contribute less estimator variance.

The method is a form of [[Reinforcement Learning]] with continuous actions and terminal rewards. The appendix also proposes, but does not benchmark, a layerwise extension with intermediate fidelity measurements and discounted future returns; that extension would add measurement overhead proportional to circuit depth.

# References

[[2022 - Policy Gradient Approach to Compilation of Variational Quantum Circuits.pdf]]
