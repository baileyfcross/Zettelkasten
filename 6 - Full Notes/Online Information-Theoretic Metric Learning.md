2026-09-14 21:00

Status: #baby

Tags: [[Distance Metric Learning]]

# Online Information-Theoretic Metric Learning

Online information-theoretic metric learning updates a Mahalanobis matrix when pairwise constraints arrive sequentially. Each step changes the current metric enough to satisfy the new similarity or dissimilarity bound while limiting information-theoretic divergence from the previous matrix.

The update supports streaming supervision without solving the full batch problem again. Its order-sensitive path makes constraint quality and step control important to stability.

# References

[[dataclassification.pdf]]
