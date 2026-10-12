2026-10-11 12:45

Status: #baby

Tags: [[Text Feature Representation]]

# Feature Selection for Sparse Text

Feature selection for sparse text retains vocabulary dimensions that contribute useful variation or class discrimination while discarding terms that are ubiquitous, extremely rare, or weakly related to the target. The reduction can lower memory use and improve the signal presented to a classifier or clusterer.

Frequency thresholds, [[TF-IDF Weighting]], and supervised scoring provide different selection criteria. Selection must be learned from training data only when evaluating prediction, because using held-out labels or frequencies would contaminate the test result.

# References

[[textminingandvisualization.pdf]]
