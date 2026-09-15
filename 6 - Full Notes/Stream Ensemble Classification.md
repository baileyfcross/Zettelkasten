2026-09-14 21:00

Status: #baby

Tags: [[Streaming and Scalable Classification]]

# Stream Ensemble Classification

Stream ensemble classification combines incrementally trained base models and changes their weights or membership according to recent performance. Components trained during different periods provide alternative views of an evolving distribution.

Replacing weak members allows adaptation without rebuilding the entire classifier at once. Diversity remains important: an ensemble of models that fail on the same drift offers little protection beyond a single learner.

# References

[[dataclassification.pdf]]
