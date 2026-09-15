2026-09-06 18:44

Status: #baby

Tags: [[Regression Model Development]] · [[Linear Model Design and Contrasts]]

# Regression Interaction Term

A regression interaction term represents a relationship in which the effect of one explanatory variable depends on the level of another. It is commonly formed as a product while retaining the corresponding lower-order terms.

Once an interaction is included, the lower-order coefficients cannot be interpreted as universal effects. Estimates become stratum-specific combinations of coefficients, so unplanned interaction searches can both inflate false positives and make the model difficult to communicate.

The source constructs interaction columns by multiplying existing design-matrix columns. In R formula syntax, `type:leg` adds only the product terms, while `type*leg` expands to both main effects and their interaction.

# References

[[analyzinghealthdatainrforsasusers.pdf]]

[[dataanalysisforthelifescienceswithr.pdf]]
