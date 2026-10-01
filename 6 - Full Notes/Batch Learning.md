2026-09-06 22:42

Status: #baby

Tags: [[Parallel Neural Network Training]]

# Batch Learning

Batch learning calculates model updates from a collection of training examples rather than changing weights after every single example. Grouping examples exposes parallel work and can make memory access and communication more efficient.

Batch size affects runtime, memory use, update frequency, and optimization behavior. A large batch is not automatically better if it delays useful parameter updates or exceeds local memory.

The extremes are fitting from the complete stored dataset at once and [[Online Learning|updating from one arriving example]]. Mini-batches use small collections per update, exposing efficient parallel calculation while changing parameters more frequently than full-batch fitting. The choice affects computation and responsiveness as well as the path followed during optimization.

# References

[[bigdatamanagementandprocessing.pdf]]

[[machinelearning_mit.epub]]
