2026-09-06 21:47

Status: #baby

Tags: [[Recursive Bayesian Estimation]]

# Bayesian Filter

A Bayesian filter estimates a changing hidden state by combining a transition model with an observation model. At each step it predicts the new state from the previous posterior, then corrects that prediction with the latest observation.

This recursion compresses earlier evidence into the current belief distribution. Different assumptions about state spaces, distributions, and inference produce special cases such as Kalman and particle filters.

# References

[[bayesianprogramming.pdf]]
