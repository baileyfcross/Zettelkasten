2026-09-13 10:20

Status: #baby

Tags: [[Classification and Decision Trees]]

# Decision Tree

A decision tree represents classification as a hierarchy of attribute tests. Internal nodes test features, branches correspond to outcomes, and leaf nodes return class labels.

Every root-to-leaf path can be read as an if-then rule. Tree depth and branching affect storage, search cost, and interpretability.

The book fits a classification tree as an interpretable baseline, examines its splits and variable importance, and applies it to held-out data. The contrast between training and validation results shows why readable structure does not eliminate the need for independent evaluation.

Each split directs an input toward a more homogeneous region, and a leaf predicts from the similar training cases that reach it. The learned structure grows with the task rather than requiring a fixed global equation. Because every path is a conjunction of tests, the fitted tree can be translated into a rule base that exposes the conditions behind a decision.

# References

[[clusteranalysisanddatamining.pdf]]

[[essentialsofdatascience.pdf]]

[[machinelearning_mit.epub]]
