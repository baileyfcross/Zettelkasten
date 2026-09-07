2026-09-06 21:47

Status: #baby

Tags: [[Bayesian Inference Algorithms]]

# Rejection Sampling

Rejection sampling proposes values from an easier distribution and accepts each according to a probability determined by the target-to-proposal ratio. Accepted values follow the target when the scaled proposal bounds it everywhere.

The method produces unweighted target samples, but its efficiency depends on how tightly the proposal covers the target. A loose bound causes most candidates to be rejected.

# References

[[bayesianprogramming.pdf]]
