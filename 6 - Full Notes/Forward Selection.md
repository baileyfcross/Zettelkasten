2026-09-06 18:44

Status: #baby

Tags: [[Regression Model Development]]

# Forward Selection

Forward selection begins with an empty or minimal model and adds candidate covariates one at a time. Once an added variable meets the retention criterion, the strict form keeps it through every later iteration.

This permanence can underperform when a variable's contribution changes after other covariates enter the model. [[Stepwise Selection]] relaxes the rule by allowing previously included variables to be reconsidered and removed.

Forward selection is one candidate-variable strategy, not a guarantee of the best or true model. Entry thresholds should be specified in advance, and the resulting formula still needs subject-matter coherence, assumption checks, and evaluation on evidence not used to choose its terms.

# References

[[analyzinghealthdatainrforsasusers.pdf]]

[[researchmethodsforinformationsystems.pdf]]
