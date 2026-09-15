2026-09-14 21:00

Status: #baby

Tags: [[Support Vector Classification]]

# One-Versus-Rest Classification

One-versus-rest classification reduces a multiclass task to one binary model per class. Each model separates its designated class from the union of all remaining classes.

Prediction compares the models' scores and chooses the strongest response. Training only as many models as there are classes is efficient, but the negative groups are heterogeneous and raw scores from independently fitted classifiers may not be directly comparable.

# References

[[dataclassification.pdf]]
