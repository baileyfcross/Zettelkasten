2026-09-09 03:12

Status: #baby

Tags: [[Cluster Analysis Foundations]] · [[Statistical Learning and Validation]]

# Dendrogram

A dendrogram is a tree diagram for a hierarchical clustering. Each node represents a cluster, connecting lines show which groups are nested, and the vertical level records when a merge or split occurs.

A horizontal cut through the dendrogram selects one partition from the hierarchy. The diagram makes the sequence visible, but the chosen cut still requires a stopping rule and substantive interpretation.

In the source's tissue example, leaf colors reveal whether an unsupervised hierarchy corresponds to known biological groups. Changes caused by feature scaling or by replacing all genes with leading principal components demonstrate that the tree depends on the representation and distance used.

Murtagh treats a ranked dendrogram as an ultrametric representation: the level of the first common ancestor gives a tree-derived distance between two leaves. Reversing the left and right children at a node changes the drawing order but preserves nested membership. A root-to-leaf path can also carry signed details in a hierarchical Haar transform, turning the tree into a multiscale data encoding.

# References

[[clusteranalysisanddatamining.pdf]]

[[dataanalysisforthelifescienceswithr.pdf]]

[[datasciencefoundations_geometry.pdf]]
