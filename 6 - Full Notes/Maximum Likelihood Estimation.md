2026-09-06 21:47

Status: #baby

Tags: [[Bayesian Parameter and Structure Learning]] · [[Count Models and Empirical Bayes]]

# Maximum Likelihood Estimation

Maximum likelihood estimation selects the parameter value under which the observed data has greatest probability. It converts parameter identification into an optimization problem once a parametric family has been specified.

The result is a point estimate and does not by itself retain uncertainty about nearby values. Unlike a Bayesian estimator, it does not combine the likelihood with an explicit prior over parameters.

The source illustrates the method with Poisson counts: independence turns the joint probability of all observed segment counts into a likelihood for the rate parameter, and the maximizing rate is the sample mean count. The example shows how a distributional assumption determines the optimization target.

# References

[[bayesianprogramming.pdf]]

[[dataanalysisforthelifescienceswithr.pdf]]
