2026-09-13 10:25

Status: #baby

Tags: [[Categorical Data Clustering]]

# ROCK Goodness Measure

The ROCK goodness measure scores a possible merge from the number of cross-links between two clusters, normalized for their sizes and the selected similarity threshold. It seeks merges whose link density is stronger than size alone would predict.

ROCK repeatedly selects the pair with the largest positive score. Local and global heaps can maintain those candidates efficiently.

# References

[[clusteranalysisanddatamining.pdf]]

