2026-09-15 02:18

Status: #baby

Tags: [[Machine Learning Foundations]]

# Model Underfitting

Underfitting occurs when a chosen model is too simple to represent important patterns in its data. A purely linear model cannot accurately capture a genuinely nonlinear relationship, regardless of how carefully its weights are tuned.

Kelleher frames this as one failure of [[Inductive Bias in Machine Learning]]: assumptions that are too strong prevent the learner from using useful information in the examples. The remedy is not simply to train longer; the candidate function family or representation must be capable of expressing the relationship. The opposite risk is [[Model Overfitting]], in which a flexible model learns sample-specific noise instead of generalizable structure.

Capacity can be changed through a different functional form, additional inputs, more local models, or a more expressive architecture. The useful level is the least complexity that captures the task's regularities: simplicity is valuable because it supports stability and interpretation, but not when it removes relationships necessary for prediction.

# References

[[deeplearning_mit.epub]]

[[machinelearning_mit.epub]]
