2026-09-06 18:44

Status: #baby

Tags: [[Analytic Data Preparation]] · [[Data Quality and Missing Data]]

# Missingness Indicator

A missingness indicator is a binary variable that marks whether another variable is absent or contains a code treated as unknown. It makes the distribution of missing information explicit and supports checks against the original field.

The indicator can help audit exclusions or describe a missing category, but it does not restore the missing measurement. If most outcome-positive records lack a required time value, a flag exposes a severe data limitation that imputation may not credibly solve.

The book also reviews missingness at the variable level before modeling. Fields that are entirely or largely missing may be excluded or handled explicitly, while rough imputation is reserved for exploratory workflows whose limitations are understood.

# References

[[analyzinghealthdatainrforsasusers.pdf]]

[[essentialsofdatascience.pdf]]
