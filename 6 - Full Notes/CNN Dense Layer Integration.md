2026-09-15 02:14

Status: #baby

Tags: [[Convolutional Visual Architecture]]

# CNN Dense Layer Integration

A dense layer near the end of a [[Convolutional Neural Network]] can connect each of its neurons to all outputs from earlier filters. Unlike the shared weights within a convolutional filter, each dense neuron learns its own weights for combining those inputs.

This stage lets different neurons integrate the [[CNN Filter Bank|filter bank's]] local detections in different ways, such as relating simpler visual patterns to a whole-object decision. It is not another convolution: the dense connections collect information across the filter outputs rather than repeatedly applying one kernel to neighboring patches.

# References

[[deeplearning_mit.epub]]
