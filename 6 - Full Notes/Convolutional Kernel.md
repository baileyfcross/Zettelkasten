2026-09-15 02:14

Status: #baby

Tags: [[Convolutional Visual Architecture]]

# Convolutional Kernel

A convolutional kernel is a small learned matrix of weights applied to a local image patch. At each [[CNN Receptive Field|receptive field]], the inputs are weighted and summed with the same kernel. Moving this calculation across the image records where its associated local pattern occurs.

The kernel itself performs the weighted-sum part of processing, not the nonlinear activation. A [[Convolutional Feature Map]] records its position-by-position outputs; a later activation function can then transform those values. Multiple kernels let a [[Convolutional Neural Network]] look for different features in parallel.

# References

[[deeplearning_mit.epub]]
