2026-09-14 20:21

Status: #baby

Tags: [[Statistical Learning and Validation]]

# Cross-Validation

Cross-validation divides training observations into folds, fits the model on all but one fold, and evaluates it on the held-out fold. Repeating the process across folds gives every observation an out-of-fold prediction.

The resulting error estimate supports [[Hyperparameter]] selection without treating resubstitution performance as generalization. All preprocessing and feature selection that learn from data must occur within each training fold to prevent information leakage.

# References

[[dataanalysisforthelifescienceswithr.pdf]]
