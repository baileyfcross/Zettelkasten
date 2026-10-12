2026-09-30 21:41

Status: #baby

Tags: [[Machine Translation Architectures]]

# Hybrid Machine Translation

Hybrid machine translation combines symbolic resources—such as dictionaries, morphology, and transfer rules—with statistical or neural components. A rule-based engine may use a learned language model to improve fluency, while a data-driven system may consult terminology, named-entity rules, or semantic resources to resolve a local decision.

The hybrid design is valuable when a mature linguistic system must be adapted without discarding years of authored knowledge, or when training data are sparse. It also preserves some capacity for targeted correction. Its cost is architectural complexity: modules must exchange compatible representations, and an error made early in the pipeline can propagate through later stages.

# References

[[machinetranslation.epub]]
