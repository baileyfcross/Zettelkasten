2026-09-06 18:44

Status: #baby

Tags: [[Analytic Data Preparation]] [[Web Forms and Validation]]

# Data Validation

Data validation tests whether an edited dataset has the intended values, relationships, and population before analysis. It includes schema checks, recode cross-tabs, partition counts, distribution review, missingness assessment, and bivariate comparisons that may reveal anomalies.

Validation should be encoded in the workflow rather than performed only by visual memory. A dataset can load without errors and still violate its codebook, lose records during subsetting, or contain an impossible relationship between an event and its measurement time.

In a web application, validation also checks form input before it changes persistent state. [[Client-Side Validation]] supplies immediate feedback, while [[Server-Side Validation]] remains authoritative because the browser can be bypassed. Rules that depend on stored values can be evaluated through an [[Asynchronous Validator]].

# References

[[analyzinghealthdatainrforsasusers.pdf]]

[[aspnetcore3andangular9_3ed.pdf]]
