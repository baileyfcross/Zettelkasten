2026-09-14 20:21

Status: #baby

Tags: [[High-Dimensional Inference and Multiple Testing]]

# Bonferroni Correction

The Bonferroni correction controls the [[Family-Wise Error Rate]] by comparing each of $m$ p-values with a family threshold divided by $m$. The union bound guarantees control without requiring the tests to be independent.

Its simplicity and broad validity come at a cost: when thousands of features are tested with modest sample sizes, the threshold can become so small that almost no true effects are detected.

The procedure controls the probability of any false rejection, not the expected proportion of errors in a discovery list. This makes it suitable when one false claim is unacceptable, while [[False Discovery Rate]] procedures can be substantially more powerful in exploratory screening.

# References

[[dataanalysisforthelifescienceswithr.pdf]]

[[introductiontohigh-dimensionalstatistics.pdf]]
