2026-09-14 21:00

Status: #baby

Tags: [[Text and Multimedia Classification]]

# Bernoulli Text Classification Model

A Bernoulli text classification model represents each vocabulary term by whether it is present or absent in a document. For every class, training estimates a Bernoulli probability for each binary feature.

Prediction multiplies evidence from both observed and absent words under a conditional-independence assumption. This model suits tasks where occurrence matters more than repetition, but it discards distinctions between a term appearing once and appearing many times.

# References

[[dataclassification.pdf]]
