2026-09-06 21:47

Status: #baby

Tags: [[Probability Foundations]] · [[Count Models and Empirical Bayes]]

# Bayes Theorem

Bayes theorem relates two conditional directions through the same joint probability:

$$P(H \mid E)=\frac{P(E \mid H)P(H)}{P(E)}.$$

The prior $P(H)$ is weighted by how likely the evidence is under the hypothesis, then normalized by the total probability of the evidence. The theorem does not create a model; its result depends on the hypotheses, distributions, and evidence already specified.

The source's disease-testing example shows why accuracy alone does not determine the probability of disease after a positive result. When prevalence is very low, false positives among the much larger unaffected population can dominate the posterior despite a highly accurate test.

# References

[[bayesianprogramming.pdf]]

[[dataanalysisforthelifescienceswithr.pdf]]
