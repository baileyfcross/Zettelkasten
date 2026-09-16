2026-09-16 01:05

Status: #baby

Tags: [[Text Feature Representation]]

# Phrase-Based Text Feature

A phrase-based text feature uses a multiword unit rather than a single token. Syntactic phrases, head-modifier pairs, adjacent n-grams, or statistically associated word combinations can distinguish meanings that bags of individual words collapse.

Greater specificity improves discrimination but reduces coverage because long combinations occur less often. Phrase features are therefore commonly added to single-word features, which retain broad coverage and reduce overfitting. Non-compositional expressions may instead need treatment as indivisible units.

# References

[[featureengineeringformachinelearninganddataanalytics.pdf]]
