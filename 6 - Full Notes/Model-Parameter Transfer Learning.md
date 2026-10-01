2026-09-14 21:00

Status: #baby

Tags: [[Transfer and Active Learning]]

# Model-Parameter Transfer Learning

Model-parameter transfer learning treats parameters learned in a source task as informative priors, initial values, or coupled components for a target model. The target is not forced to copy them exactly.

Regularization determines how strongly target estimates remain near the source solution. Strong coupling helps when tasks share a predictive mechanism but introduces bias when their boundaries differ in consequential ways.

In a deep network, early layers learned from a large source collection can be copied into a target network and later layers fitted for the new task. Reusing broadly useful visual features reduces the number of target parameters that must be learned, which is valuable when the target dataset is small. Transfer is warranted only when the tasks share the structure encoded by those layers.

# References

[[dataclassification.pdf]]

[[machinelearning_mit.epub]]
