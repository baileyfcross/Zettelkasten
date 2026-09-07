2026-09-06 21:47

Status: #baby

Tags: [[Bayesian Inference Algorithms]]

# Metropolis Algorithm

The Metropolis algorithm proposes a new state from the current one and accepts or rejects it using a ratio that preserves the desired target distribution. Rejections repeat the current state in the resulting Markov chain.

After a burn-in period, samples can approximate the target even when it is known only up to a normalization constant. Proposal size controls the tradeoff between frequent acceptance and effective movement through the state space.

# References

[[bayesianprogramming.pdf]]
