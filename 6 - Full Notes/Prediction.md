2026-09-06 21:47

Status: #baby

Tags: [[Recursive Bayesian Estimation]]

# Prediction

Prediction propagates a current belief through a state transition model to estimate a future hidden state. The farther the requested state lies beyond the latest observation, the more transition uncertainty can accumulate.

In the generic Bayesian filter, prediction is the question whose searched state has a positive temporal offset from the last known evidence. It can be followed by correction when a new observation arrives.

# References

[[bayesianprogramming.pdf]]
