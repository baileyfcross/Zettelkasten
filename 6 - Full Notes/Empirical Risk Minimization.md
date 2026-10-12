2026-09-29 19:17

Status: #baby

Tags: [[Statistical Learning and Validation]]

# Empirical Risk Minimization

Empirical risk minimization chooses the classifier in a hypothesis dictionary with the smallest average training loss. With zero–one loss, it directly minimizes the observed misclassification rate.

Training fit alone is not the target. The true risk of the selected rule depends on the best approximation available in the dictionary and on how much the empirical losses fluctuate across that dictionary. A larger class can reduce approximation error while increasing selection error, which connects the method to [[Vapnik-Chervonenkis Dimension]] and [[Excess Classification Risk]].

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
