2026-09-28 03:43

Status: #baby

Tags: [[Pharmaceutical Discovery Analytics]]

# Drug-Target Cold-Start Evaluation

Drug-target cold-start evaluation separates three prediction questions: missing interaction pairs among known entities, interactions for new drugs, and interactions for new targets. The book implements them by withholding individual matrix entries, complete drug rows, or complete target columns.

The row- and column-blinding settings are harder because the held-out entity has no positive training interaction. Reporting them separately prevents a strong pair-completion score from being mistaken for evidence that a model handles new compounds or proteins.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

