2026-09-14 20:21

Status: #baby

Tags: [[Statistical Learning and Validation]]

# Test Error

Test error measures prediction mistakes on observations not used to fit the model. When the [[Test Dataset]] represents the intended prediction population and has remained untouched, it estimates generalization performance.

Using test results repeatedly to tune a model makes the test set part of development and biases the estimate. Cross-validation can guide model selection while preserving a final independent evaluation.

The book separates validation-guided development from a final test evaluation. This protects the reported error from the many choices made while comparing trees, random forests, boosting models, and thresholds.

# References

[[dataanalysisforthelifescienceswithr.pdf]]

[[essentialsofdatascience.pdf]]
