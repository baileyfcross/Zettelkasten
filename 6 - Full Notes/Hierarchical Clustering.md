2026-09-09 03:12

Status: #baby

Tags: [[Hierarchical Clustering Methods]] · [[Statistical Learning and Validation]]

# Hierarchical Clustering

Hierarchical clustering constructs nested groups ranging from singleton observations to a cluster containing the complete data set. Every pair of clusters is either disjoint or one contains the other, so the structure can be represented as a [[Dendrogram]].

The hierarchy preserves possible solutions at many resolutions. A separate decision selects the level that best serves the analysis.

The source begins with one cluster per gene-expression sample and repeatedly joins the two most similar groups. A chosen linkage rule converts pairwise sample distances into distances between clusters, while the resulting tree supports exploration without assuming the tissue labels in advance.

The book adds a contrasting way to obtain hierarchy: a Baire longest-common-prefix tree reads nested bins from an encoded value in one pass, without first evaluating every pairwise distance. This can be useful for massive collections, but its groups depend on measurement precision and any projection used to create the code. Sequence-constrained agglomeration is another variant: it permits adjacent passages to merge so a tree retains chronology as well as similarity.

# References

[[clusteranalysisanddatamining.pdf]]

[[dataanalysisforthelifescienceswithr.pdf]]

[[datasciencefoundations_geometry.pdf]]
