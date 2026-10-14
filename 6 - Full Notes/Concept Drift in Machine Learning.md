2026-09-30 21:11

Status: #baby

Tags: [[Machine Learning Foundations]]

# Concept Drift in Machine Learning

Concept drift occurs when the process connecting a model's inputs and outputs changes over time, so relationships learned from older observations no longer describe current cases. A used-car price model, for example, can become inaccurate when the surrounding economy changes even if the vehicle attributes are recorded correctly.

The response is not merely to optimize the old model more intensely. The learner needs current feedback and new evidence, using [[Online Learning|incremental updating]] or a new training sample to follow the changed process. Monitoring should distinguish drift from ordinary random variation before replacing a still-useful model.

# References

[[machinelearning_mit.epub]]
