2026-09-06 22:42

Status: #baby

Tags: [[Parallel Neural Network Training]]

# Batch Learning

Batch learning calculates model updates from a collection of training examples rather than changing weights after every single example. Grouping examples exposes parallel work and can make memory access and communication more efficient.

Batch size affects runtime, memory use, update frequency, and optimization behavior. A large batch is not automatically better if it delays useful parameter updates or exceeds local memory.

# References

[[bigdatamanagementandprocessing.pdf]]
