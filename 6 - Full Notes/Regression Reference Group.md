2026-09-06 18:44

Status: #baby

Tags: [[Analytic Data Preparation]] · [[Linear Model Design and Contrasts]]

# Regression Reference Group

A regression reference group is the category against which indicator-variable coefficients are interpreted. Its observations receive zero on every indicator representing the other levels of the same categorical variable.

Choosing a plausible low-risk or otherwise meaningful group can make coefficients easier to explain. Unknown values sometimes remain in the reference group for practical reasons, but doing so changes its meaning and should be disclosed in the model presentation.

The source shows that R's design matrix omits one factor level and places its fitted mean in the intercept. Coefficients for the remaining levels then represent differences from this reference, so changing the reference changes individual coefficient meanings without changing the fitted group means.

# References

[[analyzinghealthdatainrforsasusers.pdf]]

[[dataanalysisforthelifescienceswithr.pdf]]
