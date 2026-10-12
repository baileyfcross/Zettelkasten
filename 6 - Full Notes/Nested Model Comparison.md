2026-09-06 18:44

Status: #baby

Tags: [[Regression Model Development]] · [[Linear Model Design and Contrasts]]

# Nested Model Comparison

A nested model comparison evaluates two models when the smaller model's terms are all contained in the larger one. The change in likelihood and degrees of freedom can be assessed to determine whether the added parameters materially improve fit.

This comparison can guide choices such as entering a continuous predictor directly or as several category indicators. A better-fitting complex model must still justify the additional parameters and yield a scientifically interpretable representation.

For least-squares models, the source compares the reduction in residual sum of squares with the additional degrees of freedom. Analysis of variance uses this relationship to test whether a block such as several interaction terms improves the model beyond sampling variation.

# References

[[analyzinghealthdatainrforsasusers.pdf]]

[[dataanalysisforthelifescienceswithr.pdf]]
