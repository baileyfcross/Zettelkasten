2026-09-14 21:34

Status: #baby

Tags: [[Unsupervised Feature Selection for Clustering]]

# Laplacian Score

Laplacian Score ranks a feature by its ability to keep nearby observations close after projection onto that feature. A graph represents local neighborhoods, and the graph Laplacian converts neighborhood preservation into a numerical score.

A low score indicates that the feature varies smoothly over the local data manifold. The method is label-free and efficient, but it evaluates features individually and can retain redundant attributes unless paired with an additional redundancy control.

# References

[[dataclustering.pdf]]

