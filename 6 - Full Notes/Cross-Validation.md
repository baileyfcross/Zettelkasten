2026-09-14 20:21

Status: #baby

Tags: [[Statistical Learning and Validation]] · [[R Multivariate Resampling and Survival Modeling]]

# Cross-Validation

Cross-validation divides training observations into folds, fits the model on all but one fold, and evaluates it on the held-out fold. Repeating the process across folds gives every observation an out-of-fold prediction.

The resulting error estimate supports [[Hyperparameter]] selection without treating resubstitution performance as generalization. All preprocessing and feature selection that learn from data must occur within each training fold to prevent information leakage.

For estimator selection, $V$-fold cross-validation fits every candidate on $V$ partial datasets and chooses the one with the smallest held-out prediction error. Larger $V$ increases computational cost, while very small $V$ reduces the stabilizing effect of repeated subsampling. In high-dimensional small-sample problems, partial-sample fits can be unstable and general finite-sample guarantees are difficult, motivating alternatives such as [[Complexity-Based Estimator Selection]].

The R recipe makes the prediction function and loss calculation explicit: each held-out subset is scored by a model fitted without those observations, and the errors are aggregated across folds. That separation is what makes the estimate informative; evaluating on training responses would merely restate the fitted model's resubstitution error.

# References

[[dataanalysisforthelifescienceswithr.pdf]]

[[introductiontohigh-dimensionalstatistics.pdf]]

[[rprimer.pdf]]
