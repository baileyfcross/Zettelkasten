2026-09-06 21:47

Status: #baby

Tags: [[Recursive Bayesian Estimation]]

# Particle Filter

A particle filter approximates a changing probability distribution with weighted samples. Particles are propagated through the transition model and reweighted by how well their predicted states explain each new observation.

Resampling concentrates computational effort on plausible regions of the state space. This makes nonlinear or non-Gaussian recursive estimation possible when an exact analytic update is impractical.

# References

[[bayesianprogramming.pdf]]
