2026-09-14 21:00

Status: #baby

Tags: [[Probabilistic Classification Models]]

# Naive Bayes Conditional Independence

Naive Bayes conditional independence assumes that observed features are mutually independent once the class label is known. The joint class-conditional likelihood can therefore be written as a product of separate feature likelihoods.

The assumption is deliberately strong and often false in literal terms, yet it turns a high-dimensional density estimate into tractable counts or parameter estimates. Prediction compares each class prior multiplied by its featurewise evidence.

# References

[[dataclassification.pdf]]
