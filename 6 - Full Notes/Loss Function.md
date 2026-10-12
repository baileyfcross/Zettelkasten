2026-09-06 00:13

Status: #baby

Tags: [[Optimization and Differentiation]]

# Loss Function

A loss function measures the difference between a machine-learning model's actual output and the desired output. It turns error into a numerical objective that training can minimize.

Different outputs require different measures. [[Squared Error Loss]] can compare individual values, while [[Categorical Cross-Entropy]] compares a predicted probability distribution with a target distribution. Backpropagation uses derivatives of the loss to guide parameter updates.

Kelleher uses a sum of squared errors to score how a candidate linear function fits labeled examples. Squaring prevents errors above and below their targets from canceling, and minimizing that score supplies a concrete objective for [[Gradient Descent]]. The score is also a fitness measure for comparing candidate functions; choosing the measure is part of the learning problem, not a neutral detail after the model has been built.

# References

[[algorithms.epub]]

[[deeplearning_mit.epub]]
