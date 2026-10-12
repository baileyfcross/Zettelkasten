2026-09-14 21:00

Status: #baby

Tags: [[Support Vector Classification]]

# One-Versus-One Classification

One-versus-one classification trains a binary classifier for every pair of classes. Each model sees only the observations belonging to its two designated classes.

At prediction time, pairwise decisions are combined by voting or a coupling procedure. The individual problems may be simpler than one-versus-rest contrasts, but the number of models grows quadratically with the number of classes and their outputs can conflict.

# References

[[dataclassification.pdf]]
