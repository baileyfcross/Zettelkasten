2026-09-06 21:47

Status: #baby

Tags: [[Bayesian Inference Algorithms]]

# Importance Sampling

Importance sampling draws candidates from a convenient proposal distribution and weights them by the ratio between target and proposal probabilities. The weights correct for sampling from the wrong distribution.

A proposal close to the important regions of the target yields stable estimates. A poor proposal produces a few dominant weights and wastes most samples, reducing the effective information in the computation.

# References

[[bayesianprogramming.pdf]]
