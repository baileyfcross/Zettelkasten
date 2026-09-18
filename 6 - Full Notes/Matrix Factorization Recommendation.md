2026-09-08 21:16

Status: #baby

Tags: [[ML.NET Recommendation Applications]] · [[Recommender System Evolution]]

# Matrix Factorization Recommendation

Matrix factorization learns lower-dimensional representations of two kinds of related entities, such as customers and products, from observed interactions. Their learned factors are combined to score pairs that were not directly observed.

In a co-purchase recommender, transaction relationships provide the training signal and candidate items are ranked by predicted score. The score orders recommendations but should not automatically be interpreted as a calibrated probability of purchase.

At large scale, matrix factorization summarizes a sparse user-item matrix with [[Latent Factor Model]] representations. [[Alternating Least Squares]] can fit those factors by switching between user and item updates, a structure that supports parallel execution.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]

[[frontiersofdatascience.pdf]]
