2026-09-13 10:20

Status: #baby

Tags: [[Classification and Decision Trees]]

# Naive Bayes Classifier

A naive Bayes classifier estimates a class score by multiplying the class prior by the conditional likelihood of each observed feature under that class. It predicts the class with the largest posterior-proportional product.

The method assumes the features are conditionally independent given the class. This strong simplification makes training and classification efficient; smoothing is needed when an unseen feature-class combination would otherwise give a zero product.

Classification compares the prior-weighted conditional products for all candidate classes and chooses the largest. Because this computation is regular and requires few model parameters, it can share an FPGA classification accelerator with vector-based methods even though its arithmetic differs from their similarity calculations.

# References

[[clusteranalysisanddatamining.pdf]]

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]
