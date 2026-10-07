2026-10-07 00:46

Status: #baby

Tags: [[Multi-Source Feature Selection]]

# Knowledge Representation Conversion

Knowledge representation conversion maps an external source into an internal structure that a feature-selection algorithm can consume. The external source may be a graph, annotation vocabulary, hierarchy, interaction list, or auxiliary dataset; the internal form may be sample similarity, feature relation, feature function, or sample category.

Conversion is source-dependent and carries modeling assumptions. For example, feature similarity can define a covariance used in [[Mahalanobis Distance]], while known feature functions can filter the target data before sample similarities are computed. Integration is meaningful only after those assumptions are explicit.

# References

[[spectralfeatureselectionfordatamining.pdf]]

