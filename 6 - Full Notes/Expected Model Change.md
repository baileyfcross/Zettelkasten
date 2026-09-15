2026-09-14 21:00

Status: #baby

Tags: [[Transfer and Active Learning]]

# Expected Model Change

Expected model change selects the unlabeled case whose possible label would produce the largest anticipated update to model parameters. Because the true label is unknown, the change is averaged or bounded across label possibilities using current predictions.

This criterion favors cases capable of moving the decision function, not merely cases with uncertain outputs. Parameter scale and model geometry determine how update magnitude should be measured.

# References

[[dataclassification.pdf]]
