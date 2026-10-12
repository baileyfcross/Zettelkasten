2026-09-17 09:48

Status: #baby

Tags: [[Recommender System Evolution]]

# Latent Factor Model

A latent factor model represents users and items through a smaller set of learned dimensions that explain patterns in their interactions. The dimensions are not required to correspond directly to named attributes.

A preference score is produced from the relationship between a user's factors and an item's factors. This compact representation makes large sparse matrices more tractable while preserving the regularities most useful for prediction.

The hidden dimensions can relate users even when they have not rated the same items. A learned factor might behave like an affinity for a family of themes without being explicitly named in the catalog; alignment between the user's and item's positions on that dimension then supplies evidence for a recommendation.

# References

[[frontiersofdatascience.pdf]]

[[recommendationengines.epub]]
