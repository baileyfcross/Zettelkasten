2026-09-06 18:44

Status: #baby

Tags: [[Regression Model Development]] · [[Linear Model Design and Contrasts]]

# Confounding Variable

A confounding variable is associated with both an exposure and an outcome without lying on the causal pathway between them. If it is not controlled, the observed exposure–outcome association may partly reflect the confounder's influence.

Candidate confounders should be selected from subject-matter knowledge and prior evidence before examining the target association. A variable is not established as a confounder merely because its own regression coefficient is statistically significant.

The source shows the corresponding design-matrix failure when treatment and sex are perfectly aligned. Balancing the factor combinations restores full rank, allowing the treatment and sex effects to be estimated separately rather than attributing their shared pattern arbitrarily.

# References

[[analyzinghealthdatainrforsasusers.pdf]]

[[dataanalysisforthelifescienceswithr.pdf]]
