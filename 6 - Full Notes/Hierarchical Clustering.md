2026-09-09 03:12

Status: #baby

Tags: [[Hierarchical Clustering Methods]] · [[Statistical Learning and Validation]]

# Hierarchical Clustering

Hierarchical clustering constructs nested groups ranging from singleton observations to a cluster containing the complete data set. Every pair of clusters is either disjoint or one contains the other, so the structure can be represented as a [[Dendrogram]].

The hierarchy preserves possible solutions at many resolutions. A separate decision selects the level that best serves the analysis.

The source begins with one cluster per gene-expression sample and repeatedly joins the two most similar groups. A chosen linkage rule converts pairwise sample distances into distances between clusters, while the resulting tree supports exploration without assuming the tissue labels in advance.

# References

[[clusteranalysisanddatamining.pdf]]

[[dataanalysisforthelifescienceswithr.pdf]]
