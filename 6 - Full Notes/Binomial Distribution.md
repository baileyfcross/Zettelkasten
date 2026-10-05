2026-09-14 20:21

Status: #baby

Tags: [[Count Models and Empirical Bayes]] · [[R Probability Simulation and Curve Fitting]]

# Binomial Distribution

The binomial distribution gives the probability of observing a specified number of successes in a fixed number of independent trials when every trial has the same success probability. Its parameters are the trial count and the per-trial probability.

It models biological counts such as variant-supporting reads when the trials and probability assumptions are appropriate. With many trials and a moderate expected count it approaches a normal shape, while rare events motivate a [[Rare Event Poisson Approximation]].

The student companion builds the distribution from repeated independent success-failure trials and uses R to calculate probabilities and simulate counts. Comparing generated frequencies with the theoretical probabilities illustrates both the model and the sampling variation present in a finite experiment.

# References

[[dataanalysisforthelifescienceswithr.pdf]]

[[rstudentcompanion.pdf]]
