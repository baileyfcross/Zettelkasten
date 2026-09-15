2026-09-14 20:21

Status: #baby

Tags: [[Statistical Learning and Validation]]

# Hyperparameter

A hyperparameter is a modeling choice set outside the ordinary parameter-fitting step. The neighbor count in [[K-Nearest Neighbors]], the span in LOESS, and the number of retained dimensions are examples that control flexibility or representation.

Choosing the value by minimizing training error creates optimistic bias. [[Cross-Validation]] estimates performance on held-out folds so competing hyperparameters can be compared without using the final test set for tuning.

# References

[[dataanalysisforthelifescienceswithr.pdf]]
