2026-10-04 22:20

Status: #baby

Tags: [[R Regression and Longitudinal Modeling]]

# R Formula Interface

The R formula interface describes a response and its predictors with an expression such as `y ~ x1 + x2`. Operators can add or remove terms, suppress the intercept, and introduce interactions, allowing one symbolic specification to define the design used by many statistical modeling functions.

Formula notation is not ordinary arithmetic: its operators describe model terms and are interpreted in the context of a data frame. Explicitly naming the data source and inspecting factor reference levels makes the resulting coefficient meanings easier to trace.

# References

[[rprimer.pdf]]
