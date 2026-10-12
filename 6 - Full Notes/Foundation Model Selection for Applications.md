2026-09-29 22:24

Status: #baby

Tags: [[Generative AI Model Adaptation and Serving]] [[Microsoft Foundry Data and Model Design]]

# Foundation Model Selection for Applications

Foundation-model selection compares an existing open or proprietary model with the application's task, accuracy, latency, throughput, cost, licensing, deployment, and data-residency requirements. Training a foundation model from scratch is usually far more expensive than adapting a suitable pretrained model.

The best benchmark score is not automatically the best production choice. A model must fit available accelerator memory, support the required commercial terms, remain operable at expected request volume, and leave enough business value after inference and platform cost.

Microsoft Foundry adds a governance-first selection sequence: eliminate models that cannot satisfy residency, retention, regulatory, audit, PII, version-locking, or baseline safety requirements before comparing acceptable candidates on quality, throughput, latency, and cost. Catalog metadata and leaderboards narrow the field, but a deployment-specific evaluation is still the release evidence.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

[[microsoftfoundryinaction.pdf]]
