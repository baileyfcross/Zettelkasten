2026-09-14 21:34

Status: #baby

Tags: [[Network and Uncertain Data Clustering]]

# UK-Means Clustering

UK-means represents each uncertain object through a probability distribution and assigns it to the center with the smallest expected squared distance. Cluster centers are updated from the expected contributions of their assigned objects.

Using expectation propagates positional uncertainty into the partition rather than replacing each object with one sampled or nominal point. Like ordinary K-means, it favors compact groups and can converge to a local optimum.

# References

[[dataclustering.pdf]]

