2026-09-06 00:13

Status: #baby

Tags: [[Artificial Neural Network Structure]]

# Neural Network Layer

A neural-network layer is a group of computational units occupying the same stage of an [[Artificial Neural Network]]. An input layer receives the observations, successive layers transform those values, and an output layer produces the network's final result.

A [[Hidden Layer]] lies between the external input and output. Layers may be [[Dense Layer|densely connected]] so every neuron feeds every unit in the following layer, or use specialized patterns suited to a particular task.

Kelleher notes that input-layer locations simply present stored values; they do not perform the learned weighted processing of later layers. In a dense network, all the neurons of the next layer can calculate their weighted sums together through [[Layer Matrix Computation|one vector–matrix operation]]. Counting only layers with learned weight matrices explains [[Neural Depth Counting|network depth]].

# References

[[algorithms.epub]]

[[deeplearning_mit.epub]]
