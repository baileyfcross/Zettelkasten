2026-09-29 22:24

Status: #baby

Tags: [[Generative AI Model Adaptation and Serving]]

# Direct Preference Optimization

Direct Preference Optimization trains a model from pairs of preferred and rejected responses. Its objective increases the relative probability of the preferred answer without first training a separate reward model and running a reinforcement-learning optimization loop.

The method simplifies preference alignment, but the resulting behavior reflects the sampled prompts, evaluators, and comparison criteria. Preference data therefore needs provenance and quality review, especially when cultural, safety, or domain judgments are not universal.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

