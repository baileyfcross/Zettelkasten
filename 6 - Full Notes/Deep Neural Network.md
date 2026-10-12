2026-09-05 16:28

Status: #baby

Tags: [[Artificial Neural Network Structure]]

# Deep Neural Network

A deep neural network is an [[Artificial Neural Network]] with multiple learned layers between input and output. Successive layers can transform raw features into progressively more useful internal representations.

Depth lets a system learn complex mappings used in speech and language, but it also increases demands for data, computation, and careful optimization through [[Backpropagation]].

Repeated matrix multiplication, convolution, normalization, attention, and nonlinear transformations expose parallel work that GPUs can accelerate. Model parameters, activations, optimizer state, batches, and communication then turn network depth and scale into concrete compute, memory, and data-path requirements.

Each [[Hidden Layer]] encodes a transformation of the representation produced before it. Successive layers can therefore build a hierarchy of concepts: an image network might progress from local edges to parts and then complete objects. This increasing level of abstraction is the sense in which the network and its learning are described as deep.

Kelleher counts [[Neural Depth Counting|depth]] by learned transformations: the hidden layers plus the output layer, or the number of weight matrices crossed. The input layer merely presents values. Additional depth increases representational flexibility, but it can also aggravate the [[Vanishing Gradient Problem]] unless the architecture and training setup support useful backward signals.

Deep learning reduces the need to handcraft every feature by training a hierarchy from raw input to abstract representation and final output. That advantage relies on large, varied datasets and substantial computation, and architecture still contributes domain knowledge—for example, convolution supplies image locality rather than asking a dense network to discover the two-dimensional arrangement from scratch.

# References

[[aiassistants.epub]]

[[algorithms.epub]]

[[deeplearning_mit.epub]]

[[machinelearning_mit.epub]]

[[nvidiagpuinfrastructurefundamentals.pdf]]
