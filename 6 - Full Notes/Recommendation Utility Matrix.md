2026-10-04 14:56

Status: #baby

Tags: [[Recommender System Evolution]]

# Recommendation Utility Matrix

A recommendation utility matrix arranges users along one dimension and items along the other. An observed cell records a rating, interaction, or other indication of how much utility the item had for that user; an unobserved cell is a preference the [[Recommender System]] may try to predict.

Most such matrices are sparse because each person encounters only a small portion of the available catalog. [[Collaborative Filtering]] compares rows or columns to fill gaps, while [[Matrix Factorization Recommendation]] learns compact user and item representations whose combinations estimate missing cells. The matrix is therefore both a record of past interaction and a structure for ranking future choices.

# References

[[recommendationengines.epub]]
