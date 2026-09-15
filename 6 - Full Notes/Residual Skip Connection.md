2026-09-15 02:14

Status: #baby

Tags: [[Convolutional Visual Architecture]]

# Residual Skip Connection

A skip connection sends the output of one neural-network layer directly to a later layer instead of requiring all information to pass through every intervening layer. Kelleher describes ResNet as an extension of the [[Convolutional Neural Network]] architecture that uses such connections to train very deep networks.

The bypass changes the network's information path while retaining the ordinary layered transformations. It is a structural response to the difficulty of training deep models, alongside methods such as improved initialization and activation functions. The book's 152-layer ResNet example illustrates the scale made possible by this design, not a general rule that depth alone improves accuracy.

# References

[[deeplearning_mit.epub]]
