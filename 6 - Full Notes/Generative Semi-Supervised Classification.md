2026-09-14 21:00

Status: #baby

Tags: [[Ensemble and Semi-Supervised Classification]]

# Generative Semi-Supervised Classification

Generative semi-supervised classification fits a joint model for features and labels using both labeled and unlabeled observations. Hidden labels on the unlabeled cases are inferred together with distribution parameters.

Expectation-maximization is a natural fitting pattern: infer fractional labels from the current model, then update parameters from both known and inferred assignments. Unlabeled data helps only when the assumed generative family describes the actual feature distribution adequately.

# References

[[dataclassification.pdf]]
