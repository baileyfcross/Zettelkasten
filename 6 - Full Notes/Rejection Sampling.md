2026-09-06 21:47

Status: #baby

Tags: [[Bayesian Inference Algorithms]] [[Pseudorandom Number Generation Methods]]

# Rejection Sampling

Rejection sampling proposes values from an easier distribution and accepts each according to a probability determined by the target-to-proposal ratio. Accepted values follow the target when the scaled proposal bounds it everywhere.

The method produces unweighted target samples, but its efficiency depends on how tightly the proposal covers the target. A loose bound causes most candidates to be rejected.

If the target density is bounded by $c$ times the proposal density, a proposal is accepted with probability equal to the target-to-envelope ratio. The mean acceptance probability is $1/c$, so choosing an instrumental density that closely follows the target directly reduces wasted proposals.

# References

[[bayesianprogramming.pdf]]

[[statisticalcomputingincplusplusandr.pdf]]
