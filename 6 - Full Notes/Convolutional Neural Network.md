2026-09-05 16:28

Status: #baby

Tags: [[Convolutional Visual Architecture]]

# Convolutional Neural Network

A convolutional neural network applies learned filters across local regions of an input. Shared filter weights allow the same pattern to be detected at different positions while using fewer parameters than dense connections.

Although strongly associated with images, convolution can also find local structure in speech representations. It can complement sequence models by detecting short acoustic patterns in a [[Feature Vector|feature sequence]].

Kelleher explains the image architecture through [[CNN Receptive Field|local receptive fields]], [[Convolutional Weight Sharing|shared weights]], and a learned [[Convolutional Kernel|kernel]] that produces a [[Convolutional Feature Map|feature map]] across positions. An activation function transforms the map, and a [[CNN Pooling Layer|pooling layer]] may downsample it. A [[CNN Filter Bank|bank of filters]] detects multiple patterns; later [[CNN Dense Layer Integration|dense layers]] can combine those responses for a whole-object decision. [[Residual Skip Connection|Skip connections]] are one extension used to train very deep versions of this architecture.

# References

[[aiassistants.epub]]

[[deeplearning_mit.epub]]
