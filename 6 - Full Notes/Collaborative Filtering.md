2026-09-17 09:48

Status: #baby

Tags: [[Recommender System Evolution]]

# Collaborative Filtering

Collaborative filtering predicts a user's preference from patterns shared with other users or items. It uses the interaction matrix rather than requiring a complete description of item content.

The approach can be memory based, using the observed dataset directly, or model based, learning parameters from a training set. Sparse ratings and new users or items create difficulties because the relevant relationships may not yet be observed.

Neighborhood-based collaborative filtering separates an offline training stage from an online prediction stage. Training computes user-user or item-item similarities, while prediction combines the selected neighbors through accumulation or weighted averaging. This split also makes the two stages separate targets for [[Recommendation Hardware Acceleration]].

# References

[[frontiersofdatascience.pdf]]

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]
