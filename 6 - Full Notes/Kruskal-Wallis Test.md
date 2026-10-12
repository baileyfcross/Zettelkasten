2026-09-06 18:44

Status: #baby

Tags: [[Descriptive Health Statistics]] · [[R Statistical Testing and Model Validation]]

# Kruskal-Wallis Test

The Kruskal–Wallis test compares a continuous or ordinal response across three or more independent groups using ranks. It is a nonparametric alternative to [[One-Way ANOVA]] when parametric assumptions are not credible.

The omnibus statistic can establish that the group distributions are not all alike, but it does not identify the differing pairs. As with other rank tests, interpretation is clearest when the shapes of the group distributions are also examined.

The procedure generalizes rank-based comparison beyond two independent groups. Its nonparametric label does not remove design assumptions: independent sampling and comparable distribution shapes remain important when the result is interpreted as a shift in location.

In R, the response and group can be supplied through a formula, and the resulting rank-sum statistic is compared with its reference distribution. The group variable must be categorical; an accidental numeric interpretation can express a trend model instead of the intended omnibus comparison.

# References

[[analyzinghealthdatainrforsasusers.pdf]]

[[researchmethodsforinformationsystems.pdf]]

[[rprimer.pdf]]
