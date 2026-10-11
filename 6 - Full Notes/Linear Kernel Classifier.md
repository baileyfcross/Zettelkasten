2026-09-14 21:00

Status: #baby

Tags: [[Support Vector Classification]]

# Linear Kernel Classifier

A linear kernel classifier uses the ordinary dot product between feature vectors. In an SVM, this produces a hyperplane directly in the original feature space.

The linear kernel is especially attractive for sparse, high-dimensional data because it avoids expensive nonlinear similarity calculations and yields a compact weight vector. Its limitation is representational: classes that require a curved boundary cannot be separated without changing the features.

For movie-review and stock-message sentiment examples, a linear support vector classifier can be trained directly on sparse text features and compared through per-class precision and recall. Strong aggregate performance does not remove the need to inspect which class remains difficult.

# References

[[dataclassification.pdf]]

[[textminingandvisualization.pdf]]
