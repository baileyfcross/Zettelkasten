2026-10-04 22:56

Status: #baby

Tags: [[R Probability Simulation and Curve Fitting]]

# Bernoulli Trial

A Bernoulli trial has two outcomes, conventionally coded as success and failure, with constant success probability $p$. Its numeric indicator has expected value $p$, so the average of repeated independent indicators estimates the underlying success probability.

R can generate the indicator by comparing uniform random values with $p$ or by drawing from a binomial distribution with one trial. Independence and constant probability are model assumptions, not consequences of the zero-one coding.

# References

[[rstudentcompanion.pdf]]
