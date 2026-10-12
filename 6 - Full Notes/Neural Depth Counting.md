2026-09-15 02:20

Status: #baby

Tags: [[Artificial Neural Network Structure]]

# Neural Depth Counting

The depth of a feedforward [[Deep Neural Network|neural network]] counts learned layers rather than merely every visible row of its diagram. The input layer presents values but has no preceding weight matrix of its own; hidden layers and the output layer perform learned transformations. Kelleher therefore counts depth as hidden layers plus the output layer, or equivalently the number of weight matrices traversed.

This convention clarifies why a diagram with one input layer, three hidden layers, and one output layer has depth four. It also makes a [[Time-Unrolled Recurrent Network|time-unrolled recurrent network]] appear deep across a long sequence even though its recurrent weights are reused at every time step.

# References

[[deeplearning_mit.epub]]
