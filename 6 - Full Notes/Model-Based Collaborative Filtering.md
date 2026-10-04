2026-09-17 09:48

Status: #baby

Tags: [[Recommender System Evolution]]

# Model-Based Collaborative Filtering

Model-based collaborative filtering learns a predictive model from part of the interaction data and then uses that model to score unobserved user-item pairs. The model summarizes regularities instead of consulting the complete dataset for every prediction.

This approach can scale and generalize better than direct neighborhood lookup, but recommendations depend on the learned representation and training objective. [[Matrix Factorization Recommendation]] is a prominent model-based method.

Training condenses interaction data into parameters that can score many users and items without consulting every observation at prediction time. This can increase catalog coverage under sparsity, but the model inherits whatever the objective rewards, so greater reach does not guarantee better user outcomes.

# References

[[frontiersofdatascience.pdf]]

[[recommendationengines.epub]]
