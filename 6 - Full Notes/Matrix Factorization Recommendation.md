2026-09-08 21:16

Status: #baby

Tags: [[ML.NET Recommendation Applications]] · [[Recommender System Evolution]]

# Matrix Factorization Recommendation

Matrix factorization learns lower-dimensional representations of two kinds of related entities, such as customers and products, from observed interactions. Their learned factors are combined to score pairs that were not directly observed.

In a co-purchase recommender, transaction relationships provide the training signal and candidate items are ranked by predicted score. The score orders recommendations but should not automatically be interpreted as a calibrated probability of purchase.

At large scale, matrix factorization summarizes a sparse user-item matrix with [[Latent Factor Model]] representations. [[Alternating Least Squares]] can fit those factors by switching between user and item updates, a structure that supports parallel execution.

The same recommendation formulation can model a [[Drug-Target Interaction Matrix]]. A logistic factorization maps drugs and proteins into a shared latent space, then adds confidence weighting and neighborhood constraints because verified interactions are more reliable than unobserved pairs.

For movie recommendations, factorization addresses a sparse matrix in which each viewer has rated few films and each film has been seen by few viewers. One factor matrix represents users as mixtures of hidden preferences and the other represents how those factors affect films. Their product predicts missing scores, and the factor count controls the complexity of the explanation even when the factors are not easy to name.

[[Singular Value Decomposition]] explains the dimensionality-reduction intuition: decomposing a utility matrix can surface latent directions that retain useful preference structure in a denser representation. The user and item factors describe compatibility along those learned directions rather than requiring every factor to be a catalog attribute chosen in advance.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]

[[frontiersofdatascience.pdf]]

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

[[machinelearning_mit.epub]]

[[recommendationengines.epub]]
