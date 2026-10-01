2026-09-30 17:53

Status: #baby

Tags: [[Large Language Model Foundations]]

# Self-Attention Mechanism

Self-attention lets every position in a sequence calculate a context-dependent mixture of value vectors from positions in that same sequence. Learned query and key projections determine which positions are relevant, while value projections provide the information that is combined.

Unlike recurrence, self-attention creates direct dependencies between distant tokens and can be computed across positions in parallel. A decoder adds a [[Causal Attention Mask]] so generation cannot use future tokens.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]
