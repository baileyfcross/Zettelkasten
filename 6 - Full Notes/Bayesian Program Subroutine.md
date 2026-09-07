2026-09-06 21:47

Status: #baby

Tags: [[Probabilistic Model Composition]]

# Bayesian Program Subroutine

A Bayesian program subroutine uses a question to one Bayesian program as the form of a distribution in another program's decomposition. Evaluating the outer factor triggers the inner inference for the current conditioning values.

The mechanism makes probabilistic models reusable without flattening every relationship into one hand-written joint distribution. The subroutine returns a distribution, so its uncertainty remains available to the calling model.

# References

[[bayesianprogramming.pdf]]
