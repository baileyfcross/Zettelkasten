2026-09-06 18:44

Status: #baby

Tags: [[Regression Model Development]] · [[Linear Model Design and Contrasts]]

# Regression Collinearity

Regression collinearity occurs when explanatory variables carry overlapping information. Their conditional coefficients and p-values can become unstable because the model has difficulty separating their individual contributions.

The symptom may appear when a covariate loses or regains significance as related terms enter the model. Thoughtful variable design, correlation review, and a second selection round can reduce redundancy, but a large sample does not automatically eliminate collinearity.

The source diagnoses exact collinearity when a design matrix has fewer independent columns than model terms. In that case, multiple coefficient vectors produce the same fitted values, so an intended effect is not uniquely estimable regardless of the fitting algorithm.

# References

[[analyzinghealthdatainrforsasusers.pdf]]

[[dataanalysisforthelifescienceswithr.pdf]]
