2026-09-14 21:00

Status: #baby

Tags: [[Rule and Instance-Based Classification]]

# CN2 Rule Induction

CN2 rule induction searches for a condition that covers a relatively pure subset of the training data, adds the resulting rule to an ordered list, and removes or downweights covered examples before continuing.

Its separate-and-conquer strategy builds one local rule at a time instead of recursively partitioning the whole space like a decision tree. Search control is needed because conjunctions of feature tests create many candidate antecedents.

# References

[[dataclassification.pdf]]
