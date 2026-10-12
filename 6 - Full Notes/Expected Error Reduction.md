2026-09-14 21:00

Status: #baby

Tags: [[Transfer and Active Learning]]

# Expected Error Reduction

Expected error reduction evaluates how much labeling a candidate is predicted to lower future generalization error. For each possible label, the learner estimates the retrained model's error and weights that result by the current label probability.

The criterion targets the final objective directly, but simulated retraining and evaluation make it computationally expensive. Approximation is often necessary when the unlabeled pool or model is large.

# References

[[dataclassification.pdf]]
