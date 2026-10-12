2026-09-15 02:14

Status: #baby

Tags: [[Convolutional Visual Architecture]]

# CNN Receptive Field

A receptive field is the limited region of an input image inspected by one neuron in a [[Convolutional Neural Network]]. Early convolutional neurons take values from small neighboring pixel patches rather than the whole image. Neurons that share a detector can be placed at different positions, so their receptive fields collectively search for the same local feature across the image.

Neighboring fields may overlap. Their separation is controlled by [[Convolutional Stride]]. Later layers can combine responses from multiple local fields into features with broader spatial scope. The field is therefore an architectural choice about which input relationships a neuron can use directly.

# References

[[deeplearning_mit.epub]]
