2026-09-06 21:47

Status: #baby

Tags: [[Bayesian Parameter and Structure Learning]]

# Bayesian Estimator

A Bayesian estimator identifies a model by calculating a posterior probability distribution over its parameters. The posterior is proportional to the data likelihood multiplied by the parameter prior.

Predictions can marginalize the parameter instead of substituting one best value. This carries identification uncertainty into later questions and supports sequential updating as observations accumulate.

The prior matters most when the sample is small; as evidence accumulates, the posterior typically concentrates more tightly around values supported by the data. When the posterior is too complicated to manipulate exactly, inference can use a tractable approximation or representative samples such as Markov chain Monte Carlo draws.

# References

[[bayesianprogramming.pdf]]

[[machinelearning_mit.epub]]
