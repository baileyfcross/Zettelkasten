2026-09-06 21:47

Status: #baby

Tags: [[Probability Foundations]] · [[Count Models and Empirical Bayes]]

# Likelihood

Likelihood evaluates how compatible observed data is with a proposed hypothesis or parameter value. Written as $P(data \mid hypothesis)$, it is viewed as a function of the hypothesis while the observed data remains fixed.

Likelihood weights prior alternatives during Bayesian inference and supplies the objective for maximum-likelihood estimation. It is not generally normalized across hypothesis values until combined with the other model factors.

For independent observations, the source multiplies their model probabilities to form a joint likelihood. Holding the observed counts fixed while varying a Poisson rate turns this expression into the function optimized by [[Maximum Likelihood Estimation]].

# References

[[bayesianprogramming.pdf]]

[[dataanalysisforthelifescienceswithr.pdf]]
