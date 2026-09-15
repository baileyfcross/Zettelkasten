2026-09-14 21:34

Status: #baby

Tags: [[Matrix Factorization and Spectral Clustering]]

# NMF Clustering Initialization

Initialization selects the starting factors from which an NMF clustering procedure begins its iterative optimization. Random nonnegative factors are simple, while SVD-based or cluster-informed starts can provide more stable structure.

Because factorization is nonconvex, initialization affects convergence speed, reconstruction error, and the resulting groups. Multiple starts and comparison of objective values or clustering stability provide a more credible solution than one arbitrary run.

# References

[[dataclustering.pdf]]

