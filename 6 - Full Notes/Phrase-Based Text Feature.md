2026-09-16 01:05

Status: #baby

Tags: [[Text Feature Representation]]

# Phrase-Based Text Feature

A phrase-based text feature uses a multiword unit rather than a single token. Syntactic phrases, head-modifier pairs, adjacent n-grams, or statistically associated word combinations can distinguish meanings that bags of individual words collapse.

Greater specificity improves discrimination but reduces coverage because long combinations occur less often. Phrase features are therefore commonly added to single-word features, which retain broad coverage and reduce overfitting. Non-compositional expressions may instead need treatment as indivisible units.

In review classification, testing unigrams, bigrams, and trigrams can change the balance between class precision and recall rather than producing a uniform improvement. The useful n-gram range is therefore an empirical feature choice that must be evaluated with the same held-out procedure as the classifier.

# References

[[featureengineeringformachinelearninganddataanalytics.pdf]]

[[textminingandvisualization.pdf]]
