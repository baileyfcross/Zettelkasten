2026-09-22 20:53

Status: #baby

Tags: [[Aggregate Consistency and Persistence]]

# Aggregate Invariant

An aggregate invariant is a condition that must remain true across the complete [[Aggregate]] after every command. It can involve several child entities and values, so individual [[Value Object]] validation is insufficient. The [[Aggregate Root]] checks the rule while performing behavior and rejects a transition that would leave the unit invalid. Rules requiring information from another aggregate do not belong in the same immediate consistency boundary unless the model is deliberately reshaped.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
