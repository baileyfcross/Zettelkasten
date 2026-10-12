2026-09-14 20:21

Status: #baby

Tags: [[Statistical Learning and Validation]]

# K-Nearest Neighbors

K-nearest neighbors predicts from the labels or outcomes of the $k$ training observations closest to a new point. For classification, the local class proportions estimate conditional probabilities and the majority supplies the predicted label.

Small $k$ creates a flexible, variable boundary, while large $k$ smooths across broader neighborhoods and can hide local structure. Feature scale and [[Dimension Reduction]] affect which observations count as nearby.

A weighted variant assigns each class the summed similarity of its members among the selected neighbors rather than using an unweighted vote. The repeated vector comparison can use a [[Reconfigurable Similarity Engine]], but storing the training set and searching it at prediction time remain the cost of this lazy-learning method.

This is a nonparametric approach to [[Model Granularity in Statistical Learning|model granularity]]: it keeps the observed cases instead of compressing them into one global formula. A numeric prediction can average the outcomes of the nearest examples. Its flexibility makes the input representation and distance definition decisive, and its prediction cost grows with the stored sample unless a search structure or approximation is used.

# References

[[dataanalysisforthelifescienceswithr.pdf]]

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

[[machinelearning_mit.epub]]
