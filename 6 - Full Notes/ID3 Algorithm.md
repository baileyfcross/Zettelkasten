2026-09-13 10:20

Status: #baby

Tags: [[Classification and Decision Trees]]

# ID3 Algorithm

ID3 recursively constructs a decision tree from categorical training data. If all examples at a node share a class it creates a leaf; otherwise it chooses the best remaining feature, branches on its values, distributes the examples, and repeats.

The best feature is selected through information gain. Basic ID3 does not directly handle numeric attributes, missing values, or noise without extensions.

# References

[[clusteranalysisanddatamining.pdf]]

