2026-09-15 02:20

Status: #baby

Tags: [[Neural Network Training]]

# Glorot Weight Initialization

Glorot initialization samples starting connection weights using a range chosen from the sizes of neighboring layers. Its aim, as Kelleher explains, is to keep the variance of activations moving forward and gradients moving backward at comparable scales across layers.

This is not a weight-training rule. It sets a better starting point before [[Backpropagation]] and [[Gradient Descent]] adjust the weights using data. The book describes its benefit as empirically supported and motivated by variance assumptions, not as a guarantee that every deep model will train successfully. Poor initial scales can worsen the [[Vanishing Gradient Problem]] or make activations and gradients difficult to use.

# References

[[deeplearning_mit.epub]]
