2026-09-16 00:09

Status: #baby

Tags: [[Classification Evaluation and Visualization]]

# Precision

Precision is the proportion of predicted positive cases that are truly positive. It answers how reliable a positive prediction is and falls when false positives increase.

Precision depends on the selected threshold and class prevalence, so it should be interpreted alongside [[Recall]] and the operational cost of false alarms.

In information retrieval, precision is the fraction of returned records that are relevant. Retrieving fewer, highly selective candidates can raise precision while leaving relevant records undiscovered, which is why the number is incomplete without recall.

For binary sentiment classification, precision should be computed separately for the positive and negative labels because each choice defines a different set of false positives. Reporting both prevents a strong majority-class result from masking unreliable predictions for the other class.

# References

[[essentialsofdatascience.pdf]]
[[machinelearning_mit.epub]]

[[textminingandvisualization.pdf]]
