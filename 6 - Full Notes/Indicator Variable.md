2026-09-06 18:44

Status: #baby

Tags: [[Analytic Data Preparation]] · [[Linear Model Design and Contrasts]]

# Indicator Variable

An indicator variable encodes membership in a category with 1 for the focal state and 0 for the comparison state. It lets a regression coefficient describe the contrast between that state and the [[Regression Reference Group]].

A categorical variable with several levels is commonly represented by several indicators while one level is omitted as the reference. Analysts should verify every indicator against its source category and avoid treating unreported values as a meaningful comparison group without justification.

In the source's design matrices, an indicator column marks whether each experimental unit belongs to a treatment or factor level. The associated coefficient becomes a difference from the omitted reference condition, making coding choices part of the model's scientific interpretation.

# References

[[analyzinghealthdatainrforsasusers.pdf]]

[[dataanalysisforthelifescienceswithr.pdf]]
