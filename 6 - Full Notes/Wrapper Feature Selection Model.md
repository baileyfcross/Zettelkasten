2026-09-14 21:00

Status: #baby

Tags: [[Classification Feature Selection]] · [[Advanced Feature Selection]]

# Wrapper Feature Selection Model

A wrapper feature selection model evaluates a candidate subset by training a predetermined classifier and measuring its predictive performance. The classifier therefore participates directly in the search for variables.

Wrappers can discover subsets well matched to a learner's inductive bias, but repeated fitting makes them expensive when the number of candidate features is large. Their estimates also require careful validation so that subset search does not overfit the evaluation data.

Wrapper selection couples a search strategy with a model-based evaluator. Sequential, randomized, or other subset searches trade coverage of the combinatorial space against the number of costly training runs.

# References

[[dataclassification.pdf]]

[[featureengineeringformachinelearninganddataanalytics.pdf]]
