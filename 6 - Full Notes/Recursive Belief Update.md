2026-09-06 21:47

Status: #baby

Tags: [[Recursive Bayesian Estimation]]

# Recursive Belief Update

A recursive belief update uses the posterior from one step as the prior for the next. A repeated transition-and-observation decomposition prevents the full observation history from having to be reconsidered from scratch.

The same description can answer filtering, prediction, or smoothing questions by changing the time index of the searched state. Its efficiency comes from the Markov assumptions encoded in the decomposition.

# References

[[bayesianprogramming.pdf]]
