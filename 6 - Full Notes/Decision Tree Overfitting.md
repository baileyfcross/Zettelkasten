2026-09-13 10:20

Status: #baby

Tags: [[Classification and Decision Trees]]

# Decision Tree Overfitting

Decision tree overfitting occurs when branches reproduce noise or accidental details of the training sample rather than a stable classification relationship. It is encouraged by small, unrepresentative, or noisy data sets.

An overfit tree can classify its training examples perfectly while performing poorly on new cases. Early stopping, pruning, validation data, statistical tests, or complexity penalties can reduce the problem.

The book demonstrates overfitting when a tree or ensemble performs exceptionally on training records but worse on validation data. Complexity and loss settings are tuned against held-out performance rather than the apparent perfection of the fitted sample.

# References

[[clusteranalysisanddatamining.pdf]]

[[essentialsofdatascience.pdf]]
