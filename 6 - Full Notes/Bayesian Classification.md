2026-09-06 21:47

Status: #baby

Tags: [[Bayesian Information Fusion]] · [[Classification and Decision Trees]]

# Bayesian Classification

Bayesian classification estimates a class variable from observed attributes by computing the posterior probability of each class. The description models how attribute values depend on the class and may include priors or dependencies among attributes.

The full posterior preserves ambiguity among classes. A later decision can choose the most probable class or use costs that distinguish different kinds of classification error.

For labeled data, the classifier combines class priors with feature likelihoods and selects the class with the largest posterior score. A naive Bayes implementation assumes conditional independence among attributes; this reduces computation but requires smoothing when an unseen feature-class combination would otherwise force a zero product.

# References

[[bayesianprogramming.pdf]]

[[clusteranalysisanddatamining.pdf]]
