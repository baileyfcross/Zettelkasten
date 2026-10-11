2026-09-14 21:00

Status: #baby

Tags: [[Classification Evaluation and Visualization]]

# Classification Validation Scheme

A classification validation scheme determines which observations train a model and which independently test its predictions. Holdout, k-fold cross-validation, repeated splits, leave-one-out procedures, and bootstrap methods make different bias, variance, and computational tradeoffs.

The split must preserve relevant class and feature distributions without leaking test information into fitting. A performance measure is meaningful only relative to the sampling and reuse pattern that produced it.

Stratified folds preserve class proportions when product reviews are imbalanced, while repeated splits show how sensitive the result is to one partition. Text vectorizers and feature selectors must be fitted inside each training fold so held-out documents remain genuinely unseen.

# References

[[dataclassification.pdf]]

[[textminingandvisualization.pdf]]
