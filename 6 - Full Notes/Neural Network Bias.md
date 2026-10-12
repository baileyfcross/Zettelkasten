2026-09-06 00:13

Status: #baby

Tags: [[Artificial Neural Network Structure]]

# Neural Network Bias

A neural-network bias is a numerical parameter added to an artificial neuron's weighted input before applying its [[Activation Function]]. It shifts the neuron's propensity to activate independently of the current input values.

The opposite of a bias can be interpreted as a threshold that the weighted sum must cross. Like a [[Neural Network Weight]], the bias is adjusted during training to reduce prediction loss.

In Kelleher's geometric example, changing the weight direction rotates a neuron's [[Decision Boundary]], while changing the bias translates that boundary away from the origin. A constant input fixed at one can treat the bias as another learned weight, allowing the same weighted-sum and matrix calculations to include it without a separate special-case update.

# References

[[algorithms.epub]]

[[deeplearning_mit.epub]]
