2026-09-30 21:11

Status: #baby

Tags: [[Machine Learning Foundations]]

# Online Learning

Online learning updates a model incrementally as individual examples or small groups arrive. It avoids requiring the complete dataset to be stored and fitted in one operation, making it suitable for a data stream or a process that continues to generate observations.

Incremental updates can also follow a slowly changing environment, but adaptation is useful only if recent evidence reflects the process that will produce future cases. Abrupt or sustained [[Concept Drift in Machine Learning|concept drift]] can make earlier examples obsolete and may require stronger forgetting, explicit detection, or retraining.

# References

[[machinelearning_mit.epub]]
