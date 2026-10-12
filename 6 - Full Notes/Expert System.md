2026-09-05 16:28

Status: #baby

Tags: [[Machine Learning Foundations]]

# Expert System

An expert system represents domain knowledge explicitly as facts and rules, then applies an inference procedure to reach conclusions. Its two central parts are a knowledge base and an inference engine.

This approach works when experts can enumerate stable rules, but it scales poorly to speech and language because acoustic and linguistic variation creates too many exceptions. [[Machine Learning]] instead learns regularities from examples.

The system's knowledge is fixed after specialists manually translate expertise into rules, which makes construction expensive and adaptation difficult. Classical true-or-false logic also handles noisy evidence, graded properties, and uncertain exceptions poorly. Probabilistic learning systems address both limitations by estimating decision rules from examples and representing uncertainty rather than requiring every condition to be exact.

# References

[[aiassistants.epub]]

[[machinelearning_mit.epub]]
