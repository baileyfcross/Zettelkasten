2026-09-06 18:44

Status: #baby

Tags: [[Regression Model Development]]

# Backward Elimination

Backward elimination begins with a model containing all candidate covariates and removes the least useful variable at each iteration until every remaining term meets a retention criterion.

Starting with the full model lets each variable be assessed conditionally on the others, but it can be difficult when many terms are collinear or the data cannot support the initial specification. Every removal should be recorded in [[Model Metadata]].

# References

[[analyzinghealthdatainrforsasusers.pdf]]
