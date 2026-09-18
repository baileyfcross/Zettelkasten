2026-09-14 21:00

Status: #baby

Tags: [[Classification Feature Selection]] · [[Advanced Feature Selection]] · [[Big Data Preprocessing]]

# Filter Feature Selection Model

A filter feature selection model scores variables from general properties of the training data before a particular classifier is fitted. Common criteria measure correlation, information, dependency, consistency, or distance between classes.

Separating selection from classifier training makes filters comparatively efficient and reduces interaction between the selector's bias and the learner's bias. The tradeoff is that a high-scoring subset may not be optimal for the eventual classification algorithm.

Within a broader taxonomy, filters contrast with wrappers, hybrids, and embedded methods. Their model independence makes them reusable and scalable, although their scoring assumptions determine which dependencies they can recognize.

For high-dimensional Big Data, filters are attractive because they avoid fitting a classifier for every candidate subset. Distributed scoring can extend that advantage, although pairwise relevance and redundancy measures may still be expensive.

# References

[[dataclassification.pdf]]

[[featureengineeringformachinelearninganddataanalytics.pdf]]

[[frontiersofdatascience.pdf]]
