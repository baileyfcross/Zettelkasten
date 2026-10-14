2026-09-14 21:00

Status: #baby

Tags: [[Ensemble and Semi-Supervised Classification]]

# AdaBoost Classification

AdaBoost classification trains weak learners sequentially while increasing the weight of examples misclassified by the current ensemble. Each learner receives a vote related to its weighted accuracy.

The procedure concentrates later models on difficult cases and combines their decisions into a stronger classifier. Its focus can also amplify mislabeled outliers, because persistently misclassified observations continue to attract weight.

AdaBoost can also be viewed as stagewise minimization of an exponential [[Convex Surrogate Classification Loss]]. This interpretation connects its example reweighting mechanism to empirical-risk optimization: each added weak rule moves the ensemble in a direction that reduces the current exponential loss.

# References

[[dataclassification.pdf]]

[[introductiontohigh-dimensionalstatistics.pdf]]
