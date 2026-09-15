2026-09-15 02:14

Status: #baby

Tags: [[Convolutional Visual Architecture]]

# Convolutional Stride

Stride length is the distance a convolutional detector moves between successive locations on an input. In the book's image example, a stride of one moves each [[CNN Receptive Field|receptive field]] one position from its neighbor, so the fields overlap substantially. Increasing stride reduces that overlap.

Stride is a [[Hyperparameter]] chosen before training rather than a kernel weight learned from data. It affects which local regions are inspected and how densely their responses appear in the [[Convolutional Feature Map]]. A larger step can make the map coarser, so the stride should match the scale of the patterns the architecture needs to preserve.

# References

[[deeplearning_mit.epub]]
