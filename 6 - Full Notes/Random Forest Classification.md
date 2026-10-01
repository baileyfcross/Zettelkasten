2026-09-14 21:00

Status: #baby

Tags: [[Ensemble and Semi-Supervised Classification]]

# Random Forest Classification

Random forest classification combines decision trees trained on bootstrap samples while considering a random subset of features at each split. Both sources of randomness promote diversity among the trees.

The final class is chosen by aggregate voting. Deep individual trees can fit complex patterns, while averaging reduces their variance; restricting candidate features prevents a few dominant predictors from making every tree too similar.

The book fits hundreds of randomized trees, monitors [[Out-of-Bag Error]], and examines variable importance before evaluating held-out probabilities. The gap between near-perfect training performance and weaker validation performance remains evidence that ensemble accuracy must be checked independently.

Randomly varying the cases and features seen by each tree creates the diversity required for useful [[Ensemble Learning]]. Voting then combines their class decisions. The improvement comes from averaging models whose mistakes differ, not from assuming that any one deep tree is a reliable explanation.

# References

[[dataclassification.pdf]]

[[essentialsofdatascience.pdf]]

[[machinelearning_mit.epub]]
