2026-09-06 00:13

Status: #baby

Tags: [[Neural Network Training]]

# Forward Propagation

Forward propagation calculates a neural network's output by moving information from the input layer toward the output layer. Each [[Artificial Neuron]] receives earlier activations, computes its weighted input and bias, and applies its activation function.

Once the final prediction is available, a [[Loss Function]] compares it with the desired output. [[Backpropagation]] then proceeds in the reverse direction to calculate how the network's parameters should change.

In Kelleher's training explanation, the forward pass records both the weighted sum and final activation for each neuron. The later backward pass needs those stored values to calculate activation derivatives and the error gradients for connection weights. Prediction and gradient calculation thus use the same forward computation, even though only training requires retaining its intermediate values for a subsequent update.

# References

[[algorithms.epub]]

[[deeplearning_mit.epub]]
