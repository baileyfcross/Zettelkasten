2026-10-12 18:17

Status: #baby

Tags: [[Policy-Gradient Variational Quantum Compilation]]

# Gaussian Policy over Variational Circuit Angles

The policy represents a variational circuit's full angle vector as a multivariate Gaussian with mean mu and covariance Sigma. A rollout samples one angle vector from that distribution, executes the corresponding circuit, and weights the sample by its [[Endpoint-Fidelity Quantum Compilation Reward]].

The mean is the paper's optimized circuit candidate. Although the log-likelihood gradient also permits learning the covariance, the reported experiments instead impose a schedule that decreases diagonal covariance from 5 x 10^-3 to 10^-6, moving from broad exploration toward concentrated exploitation.

Policy expressivity limits the best distribution the optimizer can represent, while finite rollouts create sampling error and imperfect training leaves optimization error. The covariance also changes the search dynamics: because the score-function update contains the inverse covariance, its relationship to diffusion is more subtle than simply treating larger sampling variance as a larger step.

# References

[[2022 - Policy Gradient Approach to Compilation of Variational Quantum Circuits.pdf]]
