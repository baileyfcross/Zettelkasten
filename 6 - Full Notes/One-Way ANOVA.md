2026-09-06 18:44

Status: #baby

Tags: [[Descriptive Health Statistics]] · [[R Regression and Longitudinal Modeling]]

# One-Way ANOVA

A one-way analysis of variance tests whether a continuous outcome has the same mean across levels of one explanatory variable. It partitions variability into between-group and within-group components and compares them with an F statistic.

The explanatory variable may be represented continuously or as a factor, but those specifications test different structures. A significant omnibus result shows that not all group means are equal; it does not by itself identify which groups differ.

The analysis partitions total variation into variation attributed to the factor's levels and residual variation within levels. Seen through the general linear model, it is regression with a qualitative predictor, which makes planned contrasts and assumptions about independent errors, constant variance, and residual behavior part of the same design logic.

R can express the analysis with the same formula machinery used for [[Linear Regression]]. The omnibus ANOVA table tests the factor as a whole, while post-hoc pairwise comparisons require an explicit multiplicity adjustment and should follow, not replace, examination of the fitted group means and residual assumptions.

# References

[[analyzinghealthdatainrforsasusers.pdf]]

[[researchmethodsforinformationsystems.pdf]]

[[rprimer.pdf]]
