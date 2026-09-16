2026-09-06 22:09

Status: #baby

Tags: [[Social Content Popularity Prediction]] · [[Feature Engineering and Metadata]] · [[Feature Engineering Foundations]]

# Feature Selection

Feature selection chooses a subset of observed variables for a prediction model. Removing weak or redundant inputs can reduce computation, improve interpretability, and prevent noise from obscuring useful relationships.

Selection retains original features, whereas feature extraction constructs new representations such as principal components. The appropriate method depends on feature dependence, data scale, and the prediction goal.

The book begins feature selection with role-based exclusions: identifiers, outputs, unusable missing fields, constants, high-cardinality fields, and predictors unavailable at scoring time. Algorithmic rankings are then interpreted within those data-quality and leakage constraints.

Feature selection can also make an otherwise infeasible analysis tractable by reducing a large candidate pool. Its value includes faster learning, improved accuracy when irrelevant information is removed, and greater model comprehensibility, although finding a globally optimal subset is generally computationally difficult.

# References

[[bigdataincomplexandsocialnetworks.pdf]]

[[essentialsofdatascience.pdf]]

[[featureengineeringformachinelearninganddataanalytics.pdf]]
